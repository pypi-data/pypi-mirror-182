from typing import List, Union, Optional
from os import path as osp
import re
import random
import math
import yaml
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
# from funmap.data_info import DATA_PATH_DICT, PGET_MAPPING_FILE
from IPython import embed
from sklearn.metrics import roc_curve, roc_auc_score, average_precision_score
from sklearn.metrics import precision_recall_curve
import warnings
from joblib import Parallel, delayed


def remove_version_id(value):
    if not pd.isna(value):
        return re.sub('\.\d+', '', value)
    else:
        return value


def gold_standard_edge_sets(gold_standard_file, id_type='ensembl_gene_id'):
    if id_type == 'ensembl_gene_id':
        gs_df = pd.read_csv(gold_standard_file, sep='\t')
        cols = gs_df.columns[0:2]
        gs_df.index = [tuple(sorted(x)) for x in zip(gs_df.pop(cols[0]), gs_df.pop(cols[1]))]
        gs_df = gs_df[~gs_df.index.duplicated(keep='first')]
        gs_pos_edges = set(gs_df.loc[gs_df.iloc[:, 0] == 1, :].index)
        gs_neg_edges = set(gs_df.loc[gs_df.iloc[:, 0] == 0, :].index)
    elif id_type == 'uniprot':
        gs_df = pd.read_csv(gold_standard_file)
        cols = gs_df.columns[0:2]
        gs_df.index = [tuple(sorted(x)) for x in zip(gs_df.pop(cols[0]), gs_df.pop(cols[1]))]
        gs_df = gs_df[~gs_df.index.duplicated(keep='first')]
        gs_pos_edges = set(gs_df.loc[gs_df.iloc[:, 0] == 'TP', :].index)
        gs_neg_edges = set(gs_df.loc[gs_df.iloc[:, 0] == 'FP', :].index)
    else:
        raise ValueError('id_type not supported')

    embed()
    return gs_pos_edges, gs_neg_edges


def get_data_dict(cancer_types, data_types):
    data_dict = {}
    pget_mapping = pd.read_csv(PGET_MAPPING_FILE, sep='\t')
    for ct in cancer_types:
        for dt in data_types:
            cur_feature = f'{ct}_{dt}'
            cur_file = DATA_PATH_DICT[ct][dt]
            cur_data = pd.read_csv(cur_file, sep='\t', index_col=0,
                                    header=0)
            cur_data = cur_data.T
            # remove noncoding genes first
            coding = pget_mapping.loc[pget_mapping['coding'] == 'coding', ['gene']]
            coding_genes = list(set(coding['gene'].to_list()))
            coding_genes = [x.rsplit('.', 1)[0] for x in coding_genes]
            # remove version from id if any
            cur_data = cur_data.rename(columns=lambda x: x.rsplit('.', 1)[0])
            cur_data = cur_data[[c for c in cur_data.columns if c in coding_genes]]
            # duplicated columns, for now select the last column
            cur_data = cur_data.loc[:,~cur_data.columns.duplicated(keep='last')]
            data_dict[cur_feature] = cur_data

    return data_dict


def classification_metrics(tp, fp, tn, fn):
    acc = (tp + tn) / (tp + fp + tn + fn)
    f1 = 2 * tp / (2 * tp + fp + fn)
    mcc = (tp * tn - fp * fn) / math.sqrt((tp + fp) *
                                          (tp + fn) * (tn + fp) * (tn + fn))
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    return acc, f1, mcc, precision, recall, specificity


def plot_auroc(X_y, cancer_types, data_types, output_dir):
    n_cancer_types = len(cancer_types)
    n_col = 5
    if n_cancer_types % n_col != 0:
        n_row = round(n_cancer_types/n_col) + 1
    else:
        n_row = round(n_cancer_types/n_col)
    X_y = X_y.dropna()
    for dt in data_types:
        fig, axes = plt.subplots(n_row, n_col, sharex=True, sharey=True)
        fig.set_figheight(4)
        fig.set_figwidth(10)
        for i in range(n_cancer_types):
            cur_row, cur_col = i // n_col, i % n_col
            cur_col_name = f'{cancer_types[i]}_{dt}'
            y_true = X_y['label'].values
            y_score = X_y[cur_col_name].values
            fpr, tpr, _ = roc_curve(y_true, y_score)
            roc_auc = roc_auc_score(y_true, y_score)
            axes[cur_row, cur_col].plot(fpr, tpr, color='#c51b8a', label='AUROC = %0.3f' % roc_auc)
            axes[cur_row, cur_col].plot([0, 1], [0, 1], color='#636363', linestyle='dashed')
            axes[cur_row, cur_col].legend(loc='lower right', fontsize = 'xx-small')
            axes[cur_row, cur_col].set_title(cancer_types[i])
            for pos in ['top', 'bottom', 'right', 'left']:
                axes[cur_row, cur_col].spines[pos].set_edgecolor('#bdbdbd')

        plt.setp(axes[-1, :], xlabel='FPR')
        plt.setp(axes[:, 0], ylabel='TPR')

        fig.suptitle(f'{dt}')
        plt.tight_layout()
        # one plot for each data type
        plt.savefig(osp.join(output_dir, f'auroc_{dt}_plot.pdf'))


def plot_cor(X_y, cancer_types, data_types, output_dir):
    n_cancer_types = len(cancer_types)
    # n_col = int(pow(n_cancer_types, 0.5))
    n_col = 5
    if n_cancer_types % n_col != 0:
        n_row = round(n_cancer_types/n_col) + 1
    else:
        n_row = round(n_cancer_types/n_col)
    for dt in data_types:
        fig, axes = plt.subplots(n_row, n_col, sharex=True, sharey=True)
        fig.set_figheight(4)
        fig.set_figwidth(10)
        for i in range(n_cancer_types):
            cur_row, cur_col = i // n_col, i % n_col
            cur_col_name = f'{cancer_types[i]}_{dt}'
            cur_data = X_y[[cur_col_name, 'label']]
            cur_data = cur_data.rename(columns={cur_col_name:'cor'})
            ax = sns.kdeplot(data=cur_data, x='cor', hue='label', shade=True,
                        ax=axes[cur_row, cur_col])
            axes[cur_row, cur_col].set_title(cancer_types[i])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            if cur_col != 0:
                ax.axes.yaxis.set_visible(False)
                ax.spines['left'].set_visible(False)
            if i != 0:
                ax.get_legend().remove()

        fig.suptitle(f'{dt}')
        plt.tight_layout()
        # one plot for each data type
        plt.savefig(osp.join(output_dir, f'cor_{dt}_plot.pdf'))


def eda(X_y, cancer_types, data_types, output_dir='results'):
    plot_cor(X_y, cancer_types, data_types, output_dir)
    plot_auroc(X_y, cancer_types, data_types, output_dir)


def filter_list(cancer_type: str,
                data_type: str,
                missing_threshold: float):
    cur_file = DATA_PATH_DICT[cancer_type][data_type]
    cur_data = pd.read_csv(cur_file, sep='\t', index_col=0, header=0)
    cur_data = cur_data.T
    cur_ids = list(cur_data.columns)
    cur_ids_u = list(np.unique(np.array(cur_ids)))
    if len(cur_ids) != len(cur_ids_u):
        raise ValueError('duplicated id found')
    # remove version from id
    cur_data = cur_data.rename(columns=lambda x: x.rsplit('.', 1)[0])
    # duplicated columns, for now select the last column
    cur_data = cur_data.loc[:,~cur_data.columns.duplicated(keep='last')]
    # print(cur_data.shape)
    result = cur_data.isna().mean()
    cur_data = cur_data.loc[:,result < missing_threshold]
    # print(cur_data.shape)
    return cur_data.columns


def compute_cor(edges, cancer_types, data_types,
                data_dict, pool_stats, min_valid_count, cor_func, label_val=None):
    all_features = [f'{ct}_{dt}' for ct in cancer_types
                            for dt in data_types]
    # max pooling column
    ext_cancer_types = cancer_types[:]
    ext_cancer_types.extend(pool_stats)
    col_names = [f'{ct}_{dt}' for ct in ext_cancer_types
                            for dt in data_types]
    if label_val is not None:
        col_names.append('label')
    cor_list = []
    all_indices = []
    for e in edges:
        cur_edge = tuple(sorted(e))
        values = np.empty([len(ext_cancer_types), len(data_types)])
        value_df = pd.DataFrame(values, index=ext_cancer_types, columns=data_types)
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

        # add PRO_M1, PRO_M2, PRO_M3, RNA_M1, RNA_M2, RNA_M3
        for ps in pool_stats:
            for dt in data_types:
                cur_val = value_df.loc[cancer_types, dt].values
                # sort from largest to smallest, treat na as smallest
                sorted_val = -np.sort(-cur_val)
                # split MX
                idx = int(ps[1:])
                value_df.loc[ps, dt] = sorted_val[idx-1]

        new_values = value_df.values.reshape(-1)
        # add label
        if label_val is not None:
            new_values = np.append(new_values, label_val)
        cor_list.append(list(new_values))
        all_indices.append(cur_edge)

    cor_df = pd.DataFrame(cor_list, columns=col_names, index=all_indices)
    return cor_df


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def prepare_X_y(cancer_types: List[str],
                data_types: List[str],
                pool_stats: List[str],
                edge_list_path: str,
                min_valid_count: int,
                n_jobs: int,
                neg_ratio: int=19,
                feature_type: str='cor',
                cor_type: str='pearson'
                ):
    if data_types != ['PRO', 'RNA'] and data_types != ['PRO']:
        raise ValueError('data types must be [\'PRO\',\'RNA\'] or [\'PRO\']')

    if feature_type != 'cor':
        raise ValueError('current supported feature_type: cor')

    if cor_type not in ['pearson', 'spearman']:
        raise ValueError('cor_type can be either pearson or spearman')

    label_col = 'label'
    cor_func = pearsonr if cor_type == 'pearson' else spearmanr
    ext_cancer_types = cancer_types[:]
    ext_cancer_types.extend(pool_stats)
    col_names = [f'{ct}_{dt}' for ct in ext_cancer_types
                            for dt in data_types]
    col_names.append(label_col)
    X_y = pd.DataFrame(columns=col_names)

    # edge list file contains 3 fields, Protein_1, Protein_2 and Class
    edge_df = pd.read_csv(edge_list_path, sep='\t')
    edge_df = edge_df.rename(columns={edge_df.columns[0]: 'P1',
                            edge_df.columns[1]: 'P2'})
    all_pos_edges = edge_df.loc[edge_df.iloc[:, 2] == 1, ['P1', 'P2']]
    # remove duplicated edges if any
    all_pos_edges = all_pos_edges.drop_duplicates()
    records = all_pos_edges.to_records(index=False)
    all_pos_edges = list(records)
    data_dict = {}
    for ct in cancer_types:
        for dt in data_types:
            cur_feature = f'{ct}_{dt}'
            cur_file = DATA_PATH_DICT[ct][dt]
            cur_data = pd.read_csv(cur_file, sep='\t', index_col=0,
                                    header=0)
            cur_data = cur_data.T
            cur_ids = list(cur_data.columns)
            cur_ids_u = list(np.unique(np.array(cur_ids)))
            if len(cur_ids) != len(cur_ids_u):
                raise ValueError('duplicated id found')
            # remove version from id
            cur_data = cur_data.rename(columns=lambda x: x.rsplit('.', 1)[0])
            # duplicated columns, for now select the last column
            cur_data = cur_data.loc[:,~cur_data.columns.duplicated(keep='last')]
            data_dict[cur_feature] = cur_data

    # positive
    pos_results = Parallel(n_jobs=n_jobs)(delayed(compute_cor)(edges, cancer_types, data_types,
                     data_dict, pool_stats, min_valid_count, cor_func, 1)
                      for edges in chunks(all_pos_edges, len(all_pos_edges)//n_jobs))
    for i in range(len(pos_results)):
       X_y = X_y.append(pos_results[i])


    all_neg_edges = edge_df.loc[edge_df.iloc[:, 2] == 0, ['P1', 'P2']]
    # remove duplicated edges if any
    all_neg_edges = all_neg_edges.drop_duplicates()
    records = all_neg_edges.to_records(index=False)
    all_neg_edges = list(records)
    n_pos = len(all_pos_edges)
    n_neg = len(all_neg_edges)
    print(f'Number of all positive edges {n_pos}')
    print(f'Number of all negative edges {n_neg}')
    if neg_ratio != -1:
        sampled_neg_edges = random.sample(list(all_neg_edges), n_pos * neg_ratio)
    else:
        sampled_neg_edges = list(all_neg_edges)

    print(f'Number of sampled negative edges {len(sampled_neg_edges)}')
    # negative
    neg_results = Parallel(n_jobs=n_jobs)(delayed(compute_cor)(edges,
                    cancer_types, data_types, data_dict, pool_stats, min_valid_count, cor_func, 0)
                      for edges in chunks(sampled_neg_edges, len(sampled_neg_edges)//n_jobs))

    for i in range(len(neg_results)):
       X_y = X_y.append(neg_results[i])

    return X_y



def plot_data_stats(cancer_types, data_types, output_dir='results'):
    threshold_pct = [0.1, 0.2, 0.3, 0.4, 0.5]
    valid_set = {}
    for ct in cancer_types:
        for dt in data_types:
            cur_name = f'{ct}_{dt}'
            valid_set[cur_name] = []
            for threshold in threshold_pct:
                cur_list = filter_list(ct, dt, threshold)
                valid_set[cur_name].append(len(cur_list))
    print(valid_set)
    df = pd.DataFrame.from_dict(valid_set, orient='index',
                                columns=map(str, threshold_pct))
    df.to_csv(osp.join(output_dir, 'valid_count.tsv'), sep='\t')


def count_protein(X_y):
    proteins = set()
    for i, j in X_y.index:
        proteins.add(i)
        proteins.add(j)

    return len(proteins)

def compute_auroc_and_aucpr(X_y, data_info, hash_id, output_dir='results'):
    auroc = {}
    aucpr = {}
    color = ['blue', 'orange', 'red', 'green', 'coral',
             'grey', 'indigo', 'gold', 'lime', 'olive',
             'pink', 'navy', 'magenta', 'cornflowerblue', 'tomato',
             'turquoise', 'yellowgreen', 'maroon', 'lightblue',
             'brown','teal', 'darkviolet', 'royalblue']
    X, y = X_y.iloc[:, :-1], X_y.iloc[:, -1]
    idx_pro = 0
    idx_rna = 0
    for col in X:
        cur_X = X.loc[:, col]
        cur_X_y = pd.concat([cur_X, y], axis=1)
        cur_X_y = cur_X_y.dropna()
        print(f'{col}, edge: {cur_X_y.shape[0]}, protein: {count_protein(cur_X_y)}')
        fpr, tpr, _ = roc_curve(cur_X_y.iloc[:, 1], cur_X_y.iloc[:, 0])
        roc_auc = roc_auc_score(cur_X_y.iloc[:, 1], cur_X_y.iloc[:, 0])
        auroc[col] = roc_auc
        auroc_df = pd.DataFrame.from_dict(auroc, orient='index', columns=['auroc'])
        pr, rc, _ = precision_recall_curve(cur_X_y.iloc[:, 1], cur_X_y.iloc[:, 0])
        pr_auc = average_precision_score(cur_X_y.iloc[:, 1],
                                        cur_X_y.iloc[:, 0])
        aucpr[col] = pr_auc
        aucpr_df = pd.DataFrame.from_dict(aucpr, orient='index', columns=['aucpr'])
        if 'PRO' in col:
            plt.figure('pro_auroc')
            plt.plot(fpr, tpr, color=color[idx_pro], lw=1, label=f'{col}: {roc_auc:.4f}')
            plt.figure('pro_auprc')
            plt.plot(rc, pr, color=color[idx_pro], lw=1, label=f'{col}: {pr_auc:.4f}')
            idx_pro = idx_pro + 1
        if 'RNA' in col:
            plt.figure('rna_auroc')
            plt.plot(fpr, tpr, color=color[idx_rna], lw=1, label=f'{col}: {roc_auc:.4f}')
            plt.figure('rna_auprc')
            plt.plot(rc, pr, color=color[idx_rna], lw=1, label=f'{col}: {pr_auc:.4f}')
            idx_rna = idx_rna + 1
    plt.figure('pro_auroc')
    plt.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
    plt.xlim([0, 1.0])
    plt.ylim([0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'PRO ROC Curve ({data_info["cor_type"]})')
    plt.legend(loc='lower right', ncol=3, fontsize='xx-small')
    plt.savefig(osp.join(output_dir, hash_id + '_pro_auroc_plot.pdf'))
    plt.figure('rna_auroc')
    plt.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
    plt.xlim([0, 1.0])
    plt.ylim([0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'RNA ROC Curve ({data_info["cor_type"]})')
    plt.legend(loc='lower right', ncol=3, fontsize='xx-small')
    plt.savefig(osp.join(output_dir, hash_id + '_rna_auroc_plot.pdf'))
    plt.figure('pro_auprc')
    plt.xlim([0, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'PRO PR Curve ({data_info["cor_type"]})')
    plt.legend(loc='upper right', ncol=3, fontsize='xx-small')
    plt.savefig(osp.join(output_dir, hash_id + '_pro_auprc_plot.pdf'))
    plt.figure('rna_auprc')
    plt.xlim([0, 1.0])
    plt.ylim([0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'RNA PR Curve ({data_info["cor_type"]})')
    plt.legend(loc='upper right', ncol=3, fontsize='xx-small')
    plt.savefig(osp.join(output_dir, hash_id + '_rna_auprc_plot.pdf'))

    res_df = pd.concat([auroc_df, aucpr_df], axis=1)
    res_df.to_csv(osp.join(output_dir, '_'.join([hash_id, 'auroc_auprc.tsv'])), sep='\t')

    return res_df


def save_data_info(data_info, hash_id, output_dir):
    output_file = osp.join(output_dir, '_'.join([hash_id, 'data_info.yml']))
    with open(output_file, 'w') as outfile:
        yaml.dump(data_info, outfile, default_flow_style=False)
