# using seaborn for pairplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

data = pd.read_csv('Medicalpremium.csv')

data.tail()

# missing data.
data.isna().sum()
