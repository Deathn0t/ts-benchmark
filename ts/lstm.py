import os
import time

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import tensorflow.keras as K

from ts.utils.load_data import load_training_data, minmaxstdscaler
from ts.problem import Problem
from ts.trainer import TrainerRegressorTrainValid

HERE = os.path.dirname(os.path.abspath(__file__))


(X_train, Y_train), (X_test, Y_test) = load_training_data()

Problem = Problem()
Problem.add_dim('data', {
    'X_train': X_train,
    'Y_train': Y_train,
    'X_test': X_test,
    'Y_test': Y_test
})
Problem.add_dim('preprocessing', {
    'func': minmaxstdscaler
})
Problem.add_dim('hyperparameters', {
    'batch_size': 100,
    'learning_rate': 0.01,
    'optimizer': 'adam',
    'num_epochs': 50,
    'loss_metric': 'mean_squared_error',
    'metrics': ['mean_squared_error']
})

model = None # keras model
trainer = TrainerRegressorTrainValid(Problem.space, model)

# plt.plot(l1, l2)

# n_ticks = 5
# tcks = [l1[int((i/n_ticks)*len(l1))] for i in range(n_ticks)]
# plt.xticks(ticks=tcks, labels=tcks)
# plt.show()
