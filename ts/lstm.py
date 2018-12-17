import os
import time

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import tensorflow.keras as K

from ts.utils.load_data import load_training_data

HERE = os.path.dirname(os.path.abspath(__file__))

# n_ticks = 5

t1 = time.time()
(X_train, Y_train), (X_test, Y_test) = load_training_data()
t2 = time.time()
t = t2 - t1
print('time: ', t)

# plt.plot(l1, l2)

# tcks = [l1[int((i/n_ticks)*len(l1))] for i in range(n_ticks)]
# plt.xticks(ticks=tcks, labels=tcks)
# plt.show()
