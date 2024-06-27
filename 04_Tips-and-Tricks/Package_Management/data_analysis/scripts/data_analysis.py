import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def calculate_statistics(data):
    mean_value = np.mean(data['value'])
    return mean_value
