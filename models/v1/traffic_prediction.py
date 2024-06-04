from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os
import pandas as pd
import numpy as np
from models.constants import Headers, Paths, Constants
import models.functions as fn

# Test Data
learning_rate = 0.000001
epochs = 100
batch_size = 32

fn.remove_unwanted_columns(Headers.garbage_headers, Headers.needed_headers)
ds = fn.open_csv(Paths.filtered_csv)
fn.segment_dataset(ds)
