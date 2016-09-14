"""
bootcamp_utils: a collection of statistical functions
"""
import numpy as np

def ecdf(data):
    """
    Computes ECDF of provided data
    """
    x = np.sort(data)
    y = np.arange(1,len(x)+1)/len(x)

    return x,y

def draw_bs_reps(data, func=np.mean, sz = 100):
    reps = np.empty([sz,1])
    for i in range(0,sz):
        bs_samp = np.random.choice(data,size=len(data))
        reps[i] = func(bs_samp)

    conf_int = np.percentile(reps,[2.5,97.5])
    return reps,conf_int
