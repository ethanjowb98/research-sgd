import os
import pandas as pd
import numpy as np
from models.constants import Headers, Paths

def remove_unwanted_columns(garbage_headers: list, needed_headers: dict):
    if not os.path.exists(Paths.filtered_csv):
        os.mkdir(Paths.data_dir) if not os.path.exists(Paths.data_dir) else ...
        ds = open_csv(Paths.data_csv, Headers.headers)
        for h in garbage_headers:
            ds.drop(columns=h, inplace=True)
        ds.drop(ds.index[0], axis="index", inplace=True)
        for column in needed_headers.keys():
            ds[column].astype(int, copy=False)
        save_as_csv(Paths.filtered_csv)

def segment_dataset(ds: pd.DataFrame):
    if not os.path.exists(Paths.segments_dir):
        os.mkdir(Paths.segments_dir)
        for segmentID in ds["SegmentID"].unique():
            ds.loc[ds["SegmentID"] == segmentID].to_csv(Paths.segment_csv.format(segmentID), header=None, index=None)

def open_csv(path: str, labels: dict) -> pd.DataFrame:
    return pd.read_csv(path, header=None, names=list(labels.keys()), dtype=labels)

def save_as_csv(path: str, ds: pd.DataFrame):
    ds.to_csv(path, header=None, index=None)

def mse_loss(actual, predicted):
    return np.mean(np.square(actual - predicted))

def sgd_update(ind_batch, dep_batch, weights, bias, learning_rate):
    # Forward pass
    predictions = np.dot(ind_batch, weights) + bias
    # Calculate gradients
    d_loss_d_predictions = 2 * (predictions - dep_batch)  # Derivative of MSE loss w.r.t. predictions
    de_predictions_d_weights = ind_batch  # Derivative of predictions w.r.t weights
    d_loss_d_bias = np.sum(d_loss_d_predictions)  # Derivative of MSE loss w.r.t. bias

    # Update weights and bias using SGD
    weights -= learning_rate * np.mean(de_predictions_d_weights, axis=0)
    bias -= learning_rate * d_loss_d_bias

    return weights, bias

def convert_to_original(normalized_val, max_origin, min_origin):
    return float("{:.2f}".format((normalized_val * (max_origin - min_origin)) + min_origin))
