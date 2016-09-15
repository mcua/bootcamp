import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

def coeff_of_var(data):
    "Computes coefficient of variation: std/mean"

    return np.std(data)/np.abs(np.mean(data))

    
