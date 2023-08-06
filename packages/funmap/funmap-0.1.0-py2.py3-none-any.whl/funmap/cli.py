import argparse
import sys
import yaml
import os
import json
import time
import pickle
import pandas as pd
import numpy as np
from typing import Dict, Any
import hashlib
from IPython import embed
from joblib import dump, load
from pathlib import Path
from funmap.funmap import get_valid_gs_data, validation_llr, predict_all_pairs
from funmap.funmap import prepare_features, train_ml_model, prepare_gs_data


def arg_parse():
    parser = argparse.ArgumentParser(description='command line arguments.')
    parser.add_argument('-c', '--config-file', required=True,
                        help='path to experiment configuration yaml file')
    args = parser.parse_args()

    return args


# https://www.doc.ic.ac.uk/~nuric/coding/how-to-hash-a-dictionary-in-python.html
def dict_hash(dictionary: Dict[str, Any]) -> str:
    """MD5 hash of a dictionary."""
    dhash = hashlib.md5()
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


def get_config(cfg_file):
    run_cfg = {}
    model_cfg = {}
    data_cfg = {}
    with open(cfg_file, 'r') as stream:
        cfg_dict = yaml.load(stream, Loader=yaml.FullLoader)

    model_cfg['seed'] = cfg_dict['seed'] if 'seed' in cfg_dict else 42
    model_cfg['cor_type'] = 'pearson'
    model_cfg['split_by'] = 'edge'
    model_cfg['feature_set'] = 'mutual_rank'
    model_cfg['test_size'] = 0.5
    model_cfg['ml_type'] = 'xgboost'
    model_cfg['filter_before_prediction'] = True
    model_cfg['min_feature_count'] = 1
    model_cfg['filter_after_prediction'] = True
    model_cfg['filter_criterion'] = 'max'
    model_cfg['filter_threshold'] = 0.95
    model_cfg['filter_blacklist'] = True
    run_cfg['n_jobs'] = cfg_dict['n_jobs'] if 'n_jobs' in cfg_dict else 4
    run_cfg['output_edgelist'] = cfg_dict['output_edgelist'] if 'output_edgelist' \
                                in cfg_dict else False
    run_cfg['n_output_edge'] = cfg_dict['n_output_edge'] if 'n_output_edge' \
                                in cfg_dict else -1

    return run_cfg, model_cfg, data_cfg


def main():
    args = arg_parse()
    run_cfg, model_cfg, data_cfg = get_config(args.config_file)
    # cancer_types = list(DATA_PATH_DICT.keys())
    # cancer_types.sort()
    np.random.seed(model_cfg['seed'])
    feature_set = model_cfg['feature_set']
    # data_dir = cfg['data_dir']
    results_dir = 'results'
    model_dir = 'saved_models'
    prediction_dir = 'saved_predictions'
    # data_types = ['RNA', 'PRO']
    # data_types_all = ['ALL_RNA', 'ALL_PRO', 'ALL_RNA_PRO']
    ml_type = model_cfg['ml_type']
    min_feature_count = model_cfg['min_feature_count']
    filter_before_prediction = model_cfg['filter_before_prediction']
    test_size = model_cfg['test_size']
    filter_after_prediction = model_cfg['filter_after_prediction']
    filter_criterion = model_cfg['filter_criterion']
    filter_threshold = model_cfg['filter_threshold']
    filter_blacklist = model_cfg['filter_blacklist']
    n_jobs = run_cfg['n_jobs']
    output_edge_list = run_cfg['output_edgelist']
    n_output_edge = run_cfg['n_output_edge']

    all_cfg = {**run_cfg, **model_cfg, **data_cfg}
    # results will only be affected by run_cfg and model_cfg
    res_cfg = {**model_cfg, **data_cfg}
    hash_str = dict_hash(res_cfg)
    # save configuration to results folder
    results_prefix = f'results-{hash_str}'
    results_dir = os.path.join(results_dir, results_prefix)
    ml_dir = os.path.join(results_dir, 'ml')
    model_dir = os.path.join(ml_dir, model_dir)
    prediction_dir = os.path.join(ml_dir, prediction_dir)

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    if not os.path.exists(prediction_dir):
        os.makedirs(prediction_dir)

    with open(os.path.join(results_dir, 'config.json'), 'w') as fh:
        json.dump(all_cfg, fh, indent=4)


    # split by node
    # gs_train_df_by_node_file = os.path.join(data_dir, f'gold_standard_train_cor_{mf_s}_by_node.pkl.gz')
    # gs_test_pos_by_node_file_1 = os.path.join(data_dir, f'gold_standard_test_pos_{mf_s}_by_node_1.pkl.gz')
    # gs_test_neg_by_node_file_1 = os.path.join(data_dir, f'gold_standard_test_neg_{mf_s}_by_node_1.pkl.gz')
    # gs_test_pos_by_node_file_2 = os.path.join(data_dir, f'gold_standard_test_pos_{mf_s}_by_node_2.pkl.gz')
    # gs_test_neg_by_node_file_2 = os.path.join(data_dir, f'gold_standard_test_neg_{mf_s}_by_node_2.pkl.gz')
    # # split by edge
    # gs_train_df_file = os.path.join(data_dir, f'gold_standard_train_cor_{mf_s}.pkl.gz')
    # gs_test_pos_file = os.path.join(data_dir, f'gold_standard_test_pos_{mf_s}.pkl.gz')
    # gs_test_neg_file = os.path.join(data_dir, f'gold_standard_test_neg_{mf_s}.pkl.gz')

    ml_model_file = os.path.join(model_dir, 'model.pkl.gz')
    predicted_all_pairs_file = os.path.join(prediction_dir, 'predicted_all_pairs.pkl.gz')
    blacklist_file = os.path.join(data_dir, 'funmap_blacklist.txt')

    # if validation results are available, nothing to do here
    llr_res_file = os.path.join(results_dir, 'llr_res.pickle')
    if os.path.exists(llr_res_file):
        # check if the file can be loaded successfully
        with open(llr_res_file, 'rb') as fh:
            _ = pickle.load(fh)
        print(f'{llr_res_file} exists ... nothing to be done')
        return

    sys.exit(0)

    all_feature_df = None
    gs_train = gs_test_pos = gs_test_neg = None

    # check if models and predictions are available
    if os.path.exists(predicted_all_pairs_file):
        print(f'Loading predicted all pairs from {predicted_all_pairs_file}')
        predicted_all_pairs = pd.read_pickle(predicted_all_pairs_file)
        print(f'Loading predicted all pairs ... done')
    else:
        if os.path.exists(ml_model_file):
            print(f'Loading model from {ml_model_file} ...')
            ml_model = load(ml_model_file)
            print(f'Loading model ... done')
        else:
            # train an ML model to predict the label
            cur_args = {
                        'data_dir': data_dir,
                        'min_sample_count': min_sample_count,
                        'cancer_types': cancer_types,
                        'cor_type': cor_type,
                        'data_types': data_types,
                        'n_jobs': n_jobs
            }
            all_feature_df, valid_gene_list = prepare_features(**cur_args)
            cur_args = {
                'data_dir': data_dir,
                'all_feature_df': all_feature_df,
                'valid_gene_list': valid_gene_list,
                'min_feature_count': min_feature_count,
                'test_size': test_size,
                'seed': seed,
                'split_by': split_by
            }
            gs_train, gs_test_pos, gs_test_neg = prepare_gs_data(**cur_args)
            ml_model = train_ml_model(gs_train, data_types_all, ml_type, feature_set_id,
                                    impute, impute_method, missing_indicator, seed, n_jobs)
            # save model
            dump(ml_model, ml_model_file, compress=True)
            model_symlink = os.path.join(results_dir, 'model.pkl.gz')
            if not os.path.exists(model_symlink):
                Path(model_symlink).symlink_to(Path(os.path.join('../../', os.path.basename(model_dir),
                                                                    os.path.basename(ml_model_file))))
        print('Predicting for all pairs ...')
        if all_feature_df is None:
            cur_args = {
                        'data_dir': data_dir,
                        'min_sample_count': min_sample_count,
                        'cancer_types': cancer_types,
                        'cor_type': cor_type,
                        'data_types': data_types,
                        'n_jobs': n_jobs
            }
            all_feature_df, valid_gene_list = prepare_features(**cur_args)
        predicted_all_pairs = predict_all_pairs(ml_model, feature_set_id, impute,
                                                impute_method, missing_indicator,
                                                data_types_all, all_feature_df,
                                                min_feature_count,
                                                filter_before_prediction,
                                                predicted_all_pairs_file)
        print('Predicting for all pairs ... done.')
        # create a symlink to the predicted_all_pairs_file
        predict_symlink = os.path.join(results_dir, 'prediction.pkl.gz')
        if not os.path.exists(predict_symlink):
            Path(predict_symlink).symlink_to(Path(os.path.join('../../', os.path.basename(prediction_dir),
                                            os.path.basename(predicted_all_pairs_file))))

    predicted_all_pairs = predicted_all_pairs.astype('float32')

    print('Validating ...')
    if all_feature_df is None:
        cur_args = {
            'data_dir': data_dir,
            'min_sample_count': min_sample_count,
            'cancer_types': cancer_types,
            'cor_type': cor_type,
            'data_types': data_types,
            'n_jobs': n_jobs
        }
        all_feature_df, valid_gene_list = prepare_features(**cur_args)

    if gs_train is None or gs_test_pos is None or gs_test_neg is None:
        cur_args = {
            'data_dir': data_dir,
            'all_feature_df': all_feature_df,
            'valid_gene_list': valid_gene_list,
            'min_feature_count': min_feature_count,
            'test_size': test_size,
            'seed': seed,
            'split_by': split_by
        }
        gs_train, gs_test_pos, gs_test_neg = prepare_gs_data(**cur_args)

        gs_test_pos_set = set(gs_test_pos.index)
        gs_test_neg_set = set(gs_test_neg.index)
        validation_llr(all_feature_df, predicted_all_pairs, feature_set,
                    filter_after_prediction, filter_criterion, filter_threshold,
                    filter_blacklist, blacklist_file,
                    output_edge_list, n_output_edge,
                    gs_test_pos_set, gs_test_neg_set, results_dir, results_prefix)
    print('Validating ... done.')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
