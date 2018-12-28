import json
import os

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tqdm import tqdm

HERE = os.path.dirname(os.path.abspath(__file__))

def load_source_data():
    """Load training data: Train and Test datasets.
    
    Assuming that data are located at 'ts/DATA/'.

    Returns:
        tuple(tuple(X_train, Y_train), tuple(X_test, Y_test)): training data 
    """

    train_filename = "Train_SU63ISt.csv"
    path_to_file = f"{HERE}/../DATA/{train_filename}"

    #1: Datetime
    #2: Count
    dataset = pd.read_csv(path_to_file, usecols=[1, 2], engine="python")
    return dataset


def load_training_data():

    train_filename = "train.json"
    path_to_file = f"{HERE}/../DATA/{train_filename}"
    
    if not os.path.exists(path_to_file):
        dataset = load_source_data()
        
        # unit is datapoint
        input_size = 7 * 31 * 24
        output_size = 7 * 31 * 24 # fixed, need to predict for 7 months

        length = dataset.shape[0]
        data_X, data_Y = list(), list()
        print('Creating data_X, data_Y...')
        for i in tqdm(range(length-input_size-output_size)):
        # for i in tqdm(range(10)):
            data_X.append([int(dataset['Count'][j]) for j in range(i, i+input_size)])
            data_Y.append([int(dataset['Count'][j]) for j in range(i+input_size, i+input_size+output_size)])
        
        data = {
            "data_X": data_X, 
            "data_Y": data_Y
        }

        print('Saving data...')
        with open(path_to_file, "w") as f:
            json.dump(data, f)
            print(f'data_X, data_Y are saved at: {path_to_file}')
    
    else:
        with open(path_to_file, 'r') as f:
            data = json.load(f)

    data_X = np.array(data["data_X"])
    data_Y = np.array(data["data_Y"])
        
    indexes = np.array([i for i in range(np.shape(data_X)[0])])
    np.random.shuffle(indexes)
    ratio = 0.8
    length = np.shape(indexes)[0]
    cursor = int(length*ratio)
    X_train = data_X[:cursor]
    Y_train = data_Y[:cursor]
    X_test = data_X[cursor:]
    Y_test = data_Y[cursor:]

    print("shape X_train: ", np.shape(X_train))
    print("shape Y_train: ", np.shape(Y_train))
    print("shape X_test: ", np.shape(X_test))
    print("shape Y_test: ", np.shape(Y_test))
    return (X_train, Y_train), (X_test, Y_test)

def minmaxstdscaler():
    """Use MinMaxScaler then StandardScaler.

    Returns:
        preprocessor:
    """

    preprocessor = Pipeline([
        ('minmaxscaler', MinMaxScaler()),
        ('stdscaler', StandardScaler()),
    ])
    return preprocessor