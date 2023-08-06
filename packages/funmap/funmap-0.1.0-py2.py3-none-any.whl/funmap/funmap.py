from typing import List, Union, Optional
import os
import gc
import itertools
import warnings
import csv
import pickle
from collections import defaultdict, Counter
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import xgboost as xgb
# from data_info import DATA_PATH_DICT, REACTOME_GOLD_STANDARD
from IPython import embed
from joblib import Parallel, delayed, dump, load
from funmap.utils import chunks, classification_metrics
from funmap.utils import get_data_dict, gold_standard_edge_sets
from imblearn.under_sampling import RandomUnderSampler


def get_valid_gs_data(gs_path: str, valid_gene_list: List[str]):
    """
    Filter out those pairs in gold standard where one of the proteins does not
    have min_sample_count samples with valid data in any cohort
    This will save some computation time when computing correlation to avoid
    unnecessary checking.
    """
    gs_edge_df = pd.read_csv(gs_path, sep='\t')
    gs_edge_df = gs_edge_df.rename(columns={gs_edge_df.columns[0]: 'P1',
                                            gs_edge_df.columns[1]: 'P2'})
    gs_edge_df = gs_edge_df[gs_edge_df['P1'].isin(valid_gene_list) &
                            gs_edge_df['P2'].isin(valid_gene_list)]
    gs_edge_df.reset_index(drop=True, inplace=True)
    return gs_edge_df


def compute_cc(edges, cancer_types, data_types,
            data_dict, min_valid_count, cor_func):
    all_features = [f'{ct}_{dt}' for ct in cancer_types
                            for dt in data_types]
    cor_list = []
    all_indices = []
    for e in edges:
        cur_edge = tuple(sorted(e))
        values = np.empty([len(cancer_types), len(data_types)])
        value_df = pd.DataFrame(values, index=cancer_types, columns=data_types,
                                dtype=np.float32)
        for feature in all_features:
            cur_cancer_type, cur_data_type = feature.split('_')
            cur_data = data_dict[feature]
            if cur_edge[0] in cur_data and cur_edge[1] in cur_data:
                data1 = cur_data.loc[:, cur_edge[0]].values
                data2 = cur_data.loc[:, cur_edge[1]].values
                n_valid = ~np.isnan(data1) & ~np.isnan(data2)
                n_valid_count = np.sum(n_valid)
                if n_valid_count >= min_valid_count:
                    # it is ok to see PearsonRConstantInputWarning, set to np.nan
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        corr, _ = cor_func(data1[n_valid], data2[n_valid])
                        value_df.loc[cur_cancer_type, cur_data_type] = corr
                else:
                    value_df.loc[cur_cancer_type, cur_data_type] = np.nan
            else:
                value_df.loc[cur_cancer_type, cur_data_type] = np.nan

        new_values = value_df.values.reshape(-1)
        cor_list.append(list(new_values))
        all_indices.append(cur_edge)

    new_col_name = [f'{col}_CC' for col in all_features]
    cor_df = pd.DataFrame(cor_list, columns=new_col_name, index=all_indices,
                        dtype=np.float32)
    return cor_df


def extract_gs_features(gs_df: pd.DataFrame,
                all_feature_df: pd.DataFrame):
    cols = gs_df.columns[0:2]
    gs_df.index = [tuple(sorted(x)) for x in zip(gs_df.pop(cols[0]), gs_df.pop(cols[1]))]
    l_tuple = list(gs_df.index)
    feature_df = all_feature_df.loc[l_tuple, :]
    feature_df = pd.merge(gs_df, feature_df, left_index=True, right_index=True)

    return feature_df


# create all protein pairs
def generate_all_pairs(cancer_types, data_types, min_sample_count):
    # get union of the proteins in all cancer types
    if data_types != ['PRO']:
        raise ValueError('generating all paris based on PRO data only')

    data_dict = get_data_dict(cancer_types, data_types)
    all_valid_proteins = set()
    for i in data_dict:
        cur_data = data_dict[i]
        is_valid = cur_data.notna().sum() >= min_sample_count
        valid_count = np.sum(is_valid)
        valid_p = cur_data.columns[is_valid].values
        all_valid_proteins = all_valid_proteins.union(set(valid_p))
        print(f'{i} -- ')
        print(f'  # of samples: {len(cur_data.index)}')
        print(f'  # of proteins: {len(cur_data.columns)}')
        print(f'  # of proteins with at least {min_sample_count} valid samples: {valid_count}')


    all_valid_proteins = list(all_valid_proteins)
    all_valid_proteins.sort()
    # valid protein with at least min_sample_count samples in at least on cancer type
    print(f'total number of valid proteins: {len(all_valid_proteins)}')

    pair_list = []
    for i in range(len(all_valid_proteins)):
        for j in range(i + 1, len(all_valid_proteins)):
            pair_list.append([all_valid_proteins[i], all_valid_proteins[j]])

    df = pd.DataFrame(pair_list, columns=['P1', 'P2'])
    return df, all_valid_proteins


def compute_mr(cor_arr, gene_list):
    n_genes = len(gene_list)
    res_arr = np.array([1]*len(cor_arr), dtype=np.float32)

    def convert_idx(n, i, j):
        k = (n*(n-1)/2) - (n-i)*((n-i)-1)/2 + j - i - 1
        return int(k)

    for i in range(n_genes):
        arr_idx = []
        for j in range(n_genes):
            if i < j:
                arr_idx.append(convert_idx(n_genes, i, j))
            elif i > j:
                arr_idx.append(convert_idx(n_genes, j, i))

        g_cor = cor_arr[arr_idx]
        assert len(g_cor) == n_genes - 1
        n_valid = n_genes - 1 - np.count_nonzero(np.isnan(g_cor))
        tmp = pd.Series(g_cor)
        res = tmp.argsort()
        res.replace(-1, np.nan, inplace=True)
        rank = res.argsort()
        rank.replace(-1, np.nan, inplace=True)
        rank = rank.to_numpy(dtype=np.float32) / n_valid
        del tmp
        gc.collect()
        res_arr[arr_idx] = res_arr[arr_idx] * rank

    return res_arr


def compute_all_features(edge_df, valid_gene_list, cancer_types, data_types,
                        cor_type, min_sample_count, n_jobs):
    cor_func = pearsonr if cor_type == 'pearson' else spearmanr
    data_dict = get_data_dict(cancer_types, data_types)
    col_name_cc = [f'{ct}_{dt}_CC' for ct in cancer_types
                            for dt in data_types]
    cor_df = pd.DataFrame(columns=col_name_cc)
    all_edges = edge_df.rename(columns={edge_df.columns[0]: 'P1',
                            edge_df.columns[1]: 'P2'})
    all_edges = all_edges.drop_duplicates()
    records = all_edges.to_records(index=False)
    all_edges = list(records)
    n_edges = len(all_edges)
    print(f'# of edges: {n_edges}')
    # to avoid memory error, split the edges into 2 parts
    all_edges_chunks = [all_edges[:n_edges//2], all_edges[n_edges//2:]]
    print('start computing CC ...')
    for k in range(2):
        print(f'processing chunk {k+1} of 2')
        results = Parallel(n_jobs=n_jobs)(delayed(compute_cc)(edges, cancer_types,
                    data_types, data_dict, min_sample_count, cor_func)
                    for edges in chunks(all_edges_chunks[k], len(all_edges_chunks[k])//n_jobs))
        for i in range(len(results)):
            cor_df = cor_df.append(results[i])
        del results
        gc.collect()
    print('computing CC done')
    # save to temp file to reduce memory ussage
    tmp_cor_file = '/tmp/all_cor_df.fth'
    cor_df.reset_index(inplace=True)
    cor_df.to_feather(tmp_cor_file)
    print('start computing MR ...')
    col_name_mr = [f'{ct}_{dt}_MR' for ct in cancer_types
                            for dt in data_types]
    # to avoid memory error, split the edges into 4 parts
    col_chunks = []
    batch_size = 32
    for chunk in chunks(col_name_mr, batch_size):
        col_chunks.append(chunk)
    start = 0
    res_list = []
    for chunk_idx in range(len(col_chunks)):
        print(f'processing chunk {chunk_idx+1} of {len(col_chunks)}')
        # copy a list of pd.series
        cur_data = []
        cor_df = pd.read_feather(tmp_cor_file)
        cor_df.set_index('index', inplace=True)
        for k in range(len(col_chunks[chunk_idx])):
            cur_data.append(cor_df.iloc[:, start + k].to_numpy(dtype=np.float32))
        del cor_df
        gc.collect()
        results = Parallel(n_jobs=len(col_chunks[chunk_idx]))(delayed(compute_mr)(cur_data[i], j)
                    for (i, j) in zip(range(len(col_chunks[chunk_idx])),
                                    itertools.repeat(valid_gene_list)))
        print(f'processing chunk {chunk_idx+1} of {len(col_chunks)} ... done')
        for k in range(len(col_chunks[chunk_idx])):
            del cur_data[0]
        for i in range(len(results)):
            res_list.append(results[i])
        start = start + len(col_chunks[chunk_idx])
    print('computing MR done')

    print('merging results ...')
    cor_df = pd.read_feather(tmp_cor_file)
    cor_df['index'] = cor_df['index'].apply(lambda x: tuple(x))
    cor_df.set_index('index', inplace=True)
    col_name_all = col_name_cc.copy()
    col_name_all.extend(col_name_mr)
    mr_df = pd.DataFrame(0, index=cor_df.index, columns=col_name_mr, dtype=np.float32)
    for i in range(len(res_list)):
        mr_df.iloc[:, i] = res_list[i]
    feature_df = pd.DataFrame(0, index=cor_df.index, columns=col_name_all, dtype=np.float32)
    feature_df.iloc[:, :len(col_name_cc)] = cor_df.values
    feature_df.iloc[:, len(col_name_cc):] = mr_df.values
    del mr_df
    del cor_df
    gc.collect()
    os.remove(tmp_cor_file)
    print('merging results ... done')

    return feature_df


def train_ml_model(data_df, data_types_all, ml_type, feature_set_id, impute, impute_method,
                missing_indicator, seed, n_jobs):
    X, y = impute_and_sample(data_df, impute, impute_method, missing_indicator)
    if ml_type == 'rf':
        model = train_rf_model(X, y, data_types_all, feature_set_id, seed, n_jobs)
    elif ml_type == 'xgboost':
        model = train_xgboost_model(X, y, data_types_all, feature_set_id, seed, n_jobs)
    else:
        raise ValueError('invalid ml_type')

    return model


def impute_and_sample(df, impute, impute_method, missing_indicator):
    # impute missing values sample wise
    X = df.drop('Class', axis=1)
    y = df['Class']
    if impute:
        if impute_method == 'mean':
            imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        elif impute_method == 'fill_zero':
            imp = SimpleImputer(missing_values=np.nan, strategy='constant',
                                fill_value=0)
        else:
            raise ValueError('invalid impute method')
        X_imp = imp.fit_transform(X.values.T).T
        X_imp = pd.DataFrame(X_imp, columns=X.columns, index=X.index)
    # add new features that indicate the missing state of the values
        if missing_indicator:
            for col in X.columns:
                is_na = X[col].isna().astype(int)
                X_imp[f'{col}_is_missing'] = is_na
    else:
        X_imp = X

    # Combining Random Oversampling and Undersampling
    # https://tinyurl.com/2p8zhwaa
    # over = RandomOverSampler(sampling_strategy=0.1)
    # under = RandomUnderSampler(sampling_strategy=0.5)
    # X, y = over.fit_resample(X_imp, y)
    # X, y = under.fit_resample(X, y)
    under = RandomUnderSampler(sampling_strategy='majority')
    X_under, y_under = under.fit_resample(X_imp, y)
    print(f'after impute and sampling, X shape: {X_under.shape}, y shape: {y_under.shape}')
    print(Counter(y_under))
    return X_under, y_under


def feature_set_id_to_regex(data_type, set_id):
    # select proper subset of features based on id
    # data_type: ALL_RNA or ALL_PRO or ALL_RNA_PRO
    # return regex string
    assert data_type in ['ALL_RNA', 'ALL_PRO', 'ALL_RNA_PRO']
    if set_id > 6 or set_id < 1:
        raise ValueError(f'set_id must be between 1 and 6')

    if set_id == 1:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_CC.*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_CC.*'
        else:
            regex_str = f'.*_(RNA|PRO)_CC.*'
    elif set_id == 2:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_MR.*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_MR.*'
        else:
            regex_str = f'.*_(RNA|PRO)_MR.*'
    elif set_id == 3:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_(CC|MR).*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_(CC|MR).*'
        else:
            regex_str = f'.*_(RNA|PRO)_(CC|MR).*'
    elif set_id == 4:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_CC.*|.*PPI_.*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_CC.*|.*PPI_.*'
        else:
            regex_str = f'.*_(RNA|PRO)_CC.*|.*PPI_.*'
    elif set_id == 5:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_MR.*|.*PPI_.*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_MR.*|.*PPI_.*'
        else:
            regex_str = f'.*_(RNA|PRO)_MR.*|.*PPI_.*'
    elif set_id == 6:
        if data_type == 'ALL_RNA':
            regex_str = f'.*_RNA_(CC|MR).*|.*PPI_.*'
        elif data_type == 'ALL_PRO':
            regex_str = f'.*_PRO_(CC|MR).*|.*PPI_.*'
        else:
            regex_str = f'.*_(RNA|PRO)_(CC|MR).*|.*PPI_.*'

    return regex_str


def train_xgboost_model(X, y, data_types_all, feature_set_id, seed, n_jobs):
    print('training xgboost model')
    model_params = {
        'n_estimators': [50, 150, 250],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2]
    }

    model_dict = {}
    assert data_types_all == ['ALL_RNA', 'ALL_PRO', 'ALL_RNA_PRO']
    for dt in data_types_all:
        print(f'training xgboost model for {dt}')
        xgb_model = xgb.XGBClassifier(use_label_encoder=False, random_state=seed,
                                    n_jobs=n_jobs, eval_metric='logloss')
        cv = StratifiedKFold(n_splits=5, random_state=seed, shuffle=True)
        clf = GridSearchCV(xgb_model, model_params, scoring='roc_auc', cv=cv,
                        n_jobs=1)
        regex_str = feature_set_id_to_regex(dt, feature_set_id)
        X_sel = X.filter(regex=regex_str)
        print('X_sel shape: ', X_sel.shape)
        print('y shape: ', y.shape)
        model_dict[dt] = clf.fit(X_sel, y)
        print(f'training xgboost model for {dt} ... done')

    print('training xgboost model ... done')
    return model_dict


def predict_all_pairs(model, feature_set_id, impute, impute_method, missing_indicator,
                    data_types_all, all_feature_df, min_feature_count,
                    filter_before_prediction, out_name):
    # remove rows with less than min_feature_count valid features
    if filter_before_prediction:
        all_feature_df = all_feature_df[all_feature_df.iloc[:, 1:].notna().sum(axis=1)
                                >= min_feature_count]
    # impute first
    if impute:
        if impute_method == 'mean':
            imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        elif impute_method == 'fill_zero':
            imp = SimpleImputer(missing_values=np.nan, strategy='constant',
                                fill_value=0)
        else:
            raise ValueError('invalid impute method')

        # it is possible that some pairs has no correlation coefficient value
        # in any of the data types, so we need to drop those rows
        all_feature_df = all_feature_df.dropna(axis='index', how='all')
        all_feature_df_imp = imp.fit_transform(all_feature_df.values.T).T
        all_feature_df_imp = pd.DataFrame(all_feature_df_imp,
                                        columns=all_feature_df.columns,
                                        index=all_feature_df.index)
        # add new features that indicate the missing state of the values
        if missing_indicator:
            for col in all_feature_df.columns:
                is_na = all_feature_df[col].isna().astype(int)
                all_feature_df_imp[f'{col}_is_missing'] = is_na
    else:
        all_feature_df_imp = all_feature_df

    pred_df = pd.DataFrame(columns=data_types_all, index=all_feature_df_imp.index)

    for dt in data_types_all:
        regex_str = feature_set_id_to_regex(dt, feature_set_id)
        all_feature_df_imp_sel = all_feature_df_imp.filter(regex=regex_str)
        predictions = model[dt].predict_proba(all_feature_df_imp_sel)
        pred_df[dt] = predictions[:, 1]

    pred_df.to_pickle(out_name)
    return pred_df


def validation_llr(all_feature_df, predicted_all_pair, feature_set_id,
                filter_after_prediction, filter_criterion, filter_threshold,
                filter_blacklist, blacklist_file,
                output_edge_list, n_output_edge, gs_test_pos_set,
                gs_test_neg_set, output_dir, results_prefix, case_id=None, n_jobs=40):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # final results
    case_id = '_' + str(case_id) if case_id is not None else ''
    llr_res_file = os.path.join(output_dir,
                            f'llr_res_{results_prefix}{case_id}.pickle')

    data_types_all = list(predicted_all_pair.columns)
    assert data_types_all == ['ALL_RNA', 'ALL_PRO', 'ALL_RNA_PRO']

    if os.path.exists(llr_res_file):
        # check if the file can be loaded successfully
        with open(llr_res_file, 'rb') as fh:
            llr_res_dict = pickle.load(fh)
        print(f'{llr_res_file} exists ... nothing to be done')
    else:
        print('Calculating llr_res_dict ...')
        llr_res_dict = {}
        for dt in data_types_all:
            cur_col_name = dt
            print(cur_col_name)
            cur_results = predicted_all_pair[[cur_col_name]].copy()
            cur_results.sort_values(by=cur_col_name, ascending=False,
                                    inplace=True)
            if filter_after_prediction and feature_set_id == 1:
                regex_str = feature_set_id_to_regex(cur_col_name, feature_set_id)
                all_feature_df_sel = all_feature_df.filter(regex=regex_str)
                if filter_criterion == 'max' and feature_set_id == 1:
                    all_feature_df_sel.drop(all_feature_df_sel[all_feature_df_sel.abs().max(axis=1)
                                        < filter_threshold].index, inplace=True)
                elif filter_criterion == 'max2':
                    def max2(rows, threshold):
                        results = []
                        for _, row in rows.iterrows():
                            row = row[~np.isnan(row)]
                            if len(row) < 2:
                                results.append(True)
                            else:
                                second_largest = row.nlargest(2).values[-1]
                                second_smallest = row.nsmallest(2).values[-1]
                                if ((np.abs(second_largest) > threshold) or
                                    (np.abs(second_smallest) > threshold)):
                                    results.append(False)
                                else:
                                    results.append(True)
                        return results

                    # to avoid memory error, split the edges into 2 parts
                    n_rows = len(all_feature_df_sel)
                    all_feature_df_chunks = [all_feature_df_sel[:n_rows//2], all_feature_df_sel[n_rows//2:]]
                    all_results = []
                    for k in range(2):
                        print(f'processing chunk {k+1} of 2')
                        results = Parallel(n_jobs=n_jobs)(delayed(max2)(rows, filter_threshold)
                            for rows in chunks(all_feature_df_chunks[k], len(all_feature_df_chunks[k])//n_jobs))
                        for i in range(len(results)):
                            all_results.extend(results[i])
                        print(f'processing chunk {k+1} of 2 ... done')

                    assert len(all_results) == all_feature_df_sel.shape[0]
                    all_feature_df_sel.drop(all_feature_df_sel.loc[all_results, :].index, inplace=True)
                elif filter_criterion == 'mean':
                    all_feature_df_sel.drop(all_feature_df_sel[all_feature_df_sel.mean(axis=1)
                                        < filter_threshold].index, inplace=True)
                cur_results = cur_results[cur_results.index.isin(all_feature_df_sel.index)]
            elif filter_after_prediction and feature_set_id == 2:
                if filter_criterion != 'max':
                    raise ValueError('Filter criterion must be "max" for feature set 2')
                regex_str = feature_set_id_to_regex(cur_col_name, feature_set_id)
                all_feature_df_sel = all_feature_df.filter(regex=regex_str)
                all_feature_df_sel.drop(all_feature_df_sel[all_feature_df_sel.max(axis=1)
                                    < filter_threshold].index, inplace=True)
                cur_results = cur_results[cur_results.index.isin(all_feature_df_sel.index)]
            elif filter_after_prediction and feature_set_id == 3:
                if filter_criterion != 'max':
                    raise ValueError('Filter criterion must be "max" for feature set 3')
                # filter_threshold is a string with format 'XX_YY'
                ts = filter_threshold.split('_')
                if len(ts) != 2:
                    raise ValueError('for feature set 3: threshold must be in the format of XX_YY')
                threshold_cc = float(ts[0])
                threshold_mr = float(ts[1])
                # get CC features
                regex_str = feature_set_id_to_regex(cur_col_name, 1)
                all_feature_df_sel = all_feature_df.filter(regex=regex_str)
                all_feature_df_sel.drop(all_feature_df_sel[all_feature_df_sel.abs().max(axis=1)
                                    < threshold_cc].index, inplace=True)
                sel_index_cc = all_feature_df_sel.index
                regex_str = feature_set_id_to_regex(cur_col_name, 2)
                all_feature_df_sel = all_feature_df.filter(regex=regex_str)
                all_feature_df_sel.drop(all_feature_df_sel[all_feature_df_sel.max(axis=1)
                                    < threshold_mr].index, inplace=True)
                sel_index_mr = all_feature_df_sel.index
                # intersection of two list of indices
                sel_index = sel_index_cc.intersection(sel_index_mr)
                cur_results = cur_results[cur_results.index.isin(sel_index)]

            # remove any edge that is incident on any genes in the black list
            if filter_blacklist:
                bl_genes = pd.read_csv(blacklist_file, sep='\t', header=None)
                bl_genes = set(bl_genes[0].to_list())
                cur_results = cur_results.reset_index()
                cur_results[['e1', 'e2']] = pd.DataFrame(cur_results['index'].tolist(),
                                            index=cur_results.index)
                cur_results = cur_results[~(cur_results['e1'].isin(bl_genes)
                                        | cur_results['e2'].isin(bl_genes))]
                cur_results = cur_results.drop(columns=['e1', 'e2'])
                cur_results = cur_results.set_index('index')

            cnt_notna = np.count_nonzero(~np.isnan(cur_results.values))
            result_dict = defaultdict(list)
            # assume there is at last 1,000,000 non-NA values for all cases
            assert cnt_notna > 250000
            for k in range(500, 250100, 100):
                selected_edges = set(cur_results.iloc[:k, :].index)
                # print the smallest values
                print(f'the smallest values for k = {k} of {cur_col_name} '
                    f'are: {cur_results.iloc[k,:]}')
                all_nodes = { i for t in list(selected_edges) for i in t}
                # write edge list to file
                if output_edge_list and cur_col_name == 'ALL_RNA_PRO':
                    # if k < 500000 :
                    if k == n_output_edge:
                        out_dir = os.path.join(output_dir, f'networks_{results_prefix}{case_id}')
                        if not os.path.exists(out_dir):
                            os.makedirs(out_dir)
                        edge_list_file_out = os.path.join(out_dir, f'{dt}_{k}.tsv')
                        with open(edge_list_file_out, 'w') as out_file:
                            tsv_writer = csv.writer(out_file, delimiter='\t')
                            for row in list(selected_edges):
                                tsv_writer.writerow(row)
                common_pos_edges = selected_edges & gs_test_pos_set
                common_neg_edges = selected_edges & gs_test_neg_set
                llr = np.log(len(common_pos_edges) / len(common_neg_edges) / (len(gs_test_pos_set) / len(gs_test_neg_set)))
                n_node = len(all_nodes)
                result_dict['k'].append(k)
                result_dict['n'].append(n_node)
                result_dict['llr'].append(llr)
                print(f'{dt}, {k}, {n_node}, {llr}')
            llr_res_dict[cur_col_name] = pd.DataFrame(result_dict)

        with open(llr_res_file, 'wb') as fh:
            pickle.dump(llr_res_dict, fh, protocol=pickle.HIGHEST_PROTOCOL)
        print('Calculating llr_res_dict ... done')


# correlation coefficient data
def load_features(feature_file, pair_file, valid_gene_file, cancer_types, data_types,
                cor_type, min_sample_count, n_jobs):
    if os.path.isfile(feature_file) and os.path.isfile(valid_gene_file):
            print(f'Loading all features from {feature_file}')
            all_feature_df = pd.read_feather(feature_file)
            all_feature_df['index'] = all_feature_df['index'].apply(lambda x: tuple(x))
            all_feature_df.set_index('index', inplace=True)
            print(f'Loading all features from {feature_file} ... done')
            print(f'Loading all valid gene from {valid_gene_file}')
            with open(valid_gene_file, 'r') as fp:
                valid_genes = fp.read()
                valid_gene_list = valid_genes.split('\n')
                valid_gene_list = valid_gene_list[:-1]
            print(f'Loading all {len(valid_gene_list)} valid gene from {valid_gene_file} ... done')
    else:
        print(f'Computing features for all protein pairs ...')
        if not os.path.isfile(pair_file) or not os.path.isfile(valid_gene_file):
            print(f'Generating all protein pairs ...')
            edge_df, valid_gene_list = generate_all_pairs(cancer_types, ['PRO'], min_sample_count)
            edge_df.to_csv(pair_file, sep='\t', header=False, index=False)
            with open(valid_gene_file, 'w') as fp:
                for item in valid_gene_list:
                    # write each item on a new line
                    fp.write(item + '\n')
            print(f'Generating all protein pairs ... done')
        else:
            print(f'Loading all protein pairs from {pair_file} ...')
            edge_df = pd.read_csv(pair_file, sep='\t', header=None)
            print(f'Loading all protein pairs from {pair_file} ... done')
            print(f'Loading all valid gene from {valid_gene_file}')
            with open(valid_gene_file, 'r') as fp:
                valid_genes = fp.read()
                valid_gene_list = valid_genes.split('\n')
                valid_gene_list = valid_gene_list[:-1]
            print(f'Loading all valid gene from {valid_gene_file} ... done')

        all_feature_df = compute_all_features(edge_df, valid_gene_list,
                cancer_types, data_types, cor_type, min_sample_count, n_jobs)
        all_feature_df.reset_index(index=True)
        all_feature_df.to_feather(feature_file)
        print(f'Computing feature for all protein pairs ... done')

    return all_feature_df, valid_gene_list


def prepare_gs_data(**args):
# def prepare_gs_data(data_dir, cancer_types, valid_gene_list, min_sample_count, data_types,
                # cor_type, min_feature_count, test_size, seed, split_by, n_jobs):
    data_dir = args['data_dir']
    all_feature_df = args['all_feature_df']
    valid_gene_list = args['valid_gene_list']
    min_feature_count = args['min_feature_count']
    test_size = args['test_size']
    seed = args['seed']
    split_by = args['split_by']

    mf_s = str(min_feature_count)
    if split_by == 'edge':
        gs_train_file = os.path.join(data_dir, f'gold_standard_train_{mf_s}.pkl.gz')
        gs_test_pos_file = os.path.join(data_dir, f'gold_standard_test_pos_{mf_s}.pkl.gz')
        gs_test_neg_file = os.path.join(data_dir, f'gold_standard_test_neg_{mf_s}.pkl.gz')

        if (os.path.isfile(gs_train_file) and os.path.isfile(gs_test_pos_file)
            and os.path.isfile(gs_test_neg_file)):
            print(f'Loading existing data file from {gs_train_file}')
            gs_train_df = pd.read_pickle(gs_train_file)
            print(f'Loading existing data file from {gs_train_file} ... done')
            print(f'Loading existing data file from {gs_test_pos_file}')
            gs_test_pos_df = pd.read_pickle(gs_test_pos_file)
            print(f'Loading existing data file from {gs_test_pos_file} ... done')
            print(f'Loading existing data file from {gs_test_neg_file}')
            gs_test_neg_df = pd.read_pickle(gs_test_neg_file)
            print(f'Loading existing data file from {gs_test_neg_file} ... done')
        else:
            print('Preparing gs data ...')
            gs_df = get_valid_gs_data(REACTOME_GOLD_STANDARD, valid_gene_list)
            gs_X_y_train, gs_X_y_test = train_test_split(gs_df,
                                                        test_size=test_size,
                                                        random_state=seed,
                                                        stratify=gs_df[['Class']])
            gs_train_df = extract_gs_features(gs_X_y_train, all_feature_df)
            pd.to_pickle(gs_train_df, gs_train_file)
            cols = gs_X_y_test.columns[0:2]
            gs_X_y_test.index = [tuple(sorted(x)) for x in
                                zip(gs_X_y_test.pop(cols[0]),
                                    gs_X_y_test.pop(cols[1]))]

            gs_test_pos_df = gs_X_y_test.loc[gs_X_y_test['Class'] == 1, 'Class']
            gs_test_neg_df = gs_X_y_test.loc[gs_X_y_test['Class'] == 0, 'Class']
            pd.to_pickle(gs_test_pos_df, gs_test_pos_file)
            pd.to_pickle(gs_test_neg_df, gs_test_neg_file)
            print('Preparing gs data ... done')
        return gs_train_df, gs_test_pos_df, gs_test_neg_df
    elif split_by == 'node':
        # :TODO:  to be updated
        raise ValueError('currently only support split by edge')
        """
        # if (os.path.isfile(gs_train_cor_by_node_file)
        #     and os.path.isfile(gs_test_pos_by_node_file_1)
        #     and os.path.isfile(gs_test_neg_by_node_file_1)
        #     and os.path.isfile(gs_test_pos_by_node_file_2)
        #     and os.path.isfile(gs_test_neg_by_node_file_2)):
        #     print(f'Loading existing data file from {gs_train_cor_by_node_file}')
        #     train_cor_df = pd.read_pickle(gs_train_cor_by_node_file)
        #     print(f'Loading existing data file from {gs_train_cor_by_node_file} ... done')
        #     print(f'Loading existing data file from {gs_test_pos_by_node_file_1}')
        #     gs_test_pos_df_1 = pd.read_pickle(gs_test_pos_by_node_file_1)
        #     print(f'Loading existing data file from {gs_test_pos_by_node_file_1} ... done')
        #     print(f'Loading existing data file from {gs_test_neg_by_node_file_1}')
        #     gs_test_neg_df_1 = pd.read_pickle(gs_test_neg_by_node_file_1)
        #     print(f'Loading existing data file from {gs_test_neg_by_node_file_1} ... done')
        #     print(f'Loading existing data file from {gs_test_pos_by_node_file_2}')
        #     gs_test_pos_df_2 = pd.read_pickle(gs_test_pos_by_node_file_2)
        #     print(f'Loading existing data file from {gs_test_pos_by_node_file_2} ... done')
        #     print(f'Loading existing data file from {gs_test_neg_by_node_file_2}')
        #     gs_test_neg_df_2 = pd.read_pickle(gs_test_neg_by_node_file_2)
        #     print(f'Loading existing data file from {gs_test_neg_by_node_file_2} ... done')
        # else:
        #     print('Preparing data file...')
        #     gs_df = get_valid_gs_pairs(REACTOME_GOLD_STANDARD, cancer_types,
        #                             min_sample_count)
        #     p1 = set(gs_df['P1'].to_list())
        #     p2 = set(gs_df['P2'].to_list())
        #     all_p = p1.union(p2)   # number of all proteins: 5510
        #     train_p, test_p = train_test_split(list(all_p), test_size=test_size,
        #                                        random_state=seed)
        #     gs_X_y_train = gs_df.loc[gs_df['P1'].isin(train_p) & gs_df['P2'].isin(train_p)]
        #     # case 1: testing edge only between proteins in test_p
        #     gs_X_y_test_1 = gs_df.loc[gs_df['P1'].isin(test_p) & gs_df['P2'].isin(test_p)]
        #     # case 2: testing edge include all edges except those in train_df
        #     gs_X_y_test_2 = gs_df.loc[~(gs_df['P1'].isin(train_p) & gs_df['P2'].isin(train_p))]
        #     # split the nodes into train and test
        #     # training edges are from train node set
        #     # test edges are from test node set
        #     train_cor_df = compute_gs_cc(gs_X_y_train, cancer_types,
        #                         data_types, cor_type, min_sample_count,
        #                         min_feature_count, n_jobs)
        #     pd.to_pickle(train_cor_df, gs_train_cor_by_node_file)
        #     cols = gs_X_y_test_1.columns[0:2]
        #     gs_X_y_test_1.index = [tuple(sorted(x)) for x in
        #                            zip(gs_X_y_test_1.pop(cols[0]),
        #                             gs_X_y_test_1.pop(cols[1]))]
        #     gs_test_pos_df_1 = gs_X_y_test_1.loc[gs_X_y_test_1['Class'] == 1, 'Class']
        #     gs_test_neg_df_1 = gs_X_y_test_1.loc[gs_X_y_test_1['Class'] == 0, 'Class']
        #     pd.to_pickle(gs_test_pos_df_1, gs_test_pos_by_node_file_1)
        #     pd.to_pickle(gs_test_neg_df_1, gs_test_neg_by_node_file_1)
        #     cols = gs_X_y_test_2.columns[0:2]
        #     gs_X_y_test_2.index = [tuple(sorted(x)) for x in
        #                            zip(gs_X_y_test_2.pop(cols[0]),
        #                             gs_X_y_test_2.pop(cols[1]))]
        #     gs_test_pos_df_2 = gs_X_y_test_2.loc[gs_X_y_test_2['Class'] == 1, 'Class']
        #     gs_test_neg_df_2 = gs_X_y_test_2.loc[gs_X_y_test_2['Class'] == 0, 'Class']
        #     pd.to_pickle(gs_test_pos_df_2, gs_test_pos_by_node_file_2)
        #     pd.to_pickle(gs_test_neg_df_2, gs_test_neg_by_node_file_2)
        #     print('Preparing data file... done')
        """


# input featurs for all pairs
def prepare_features(**args):
    data_dir = args['data_dir']
    cancer_types = args['cancer_types']
    data_types = args['data_types']
    min_sample_count = args['min_sample_count']
    n_jobs = args['n_jobs']
    cor_type = args['cor_type']
    pair_file = os.path.join(data_dir, 'all_pairs.tsv.gz')
    valid_gene_file = os.path.join(data_dir, 'all_valid_gene.txt')
    feature_file = os.path.join(data_dir, 'all_features.fth')
    feature_df, valid_gene_list = load_features(feature_file, pair_file, valid_gene_file,
            cancer_types, data_types, cor_type, min_sample_count, n_jobs)
    return feature_df, valid_gene_list
