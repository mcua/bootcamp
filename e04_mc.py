import numpy as np
import pandas as pd
import bootcamp_utils as bu
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def backtrack_steps():

    nsteps = []
    numit  = 0
    while len(nsteps) == 0 and numit < 1000:
        steps  = np.random.random(10000)
        steps  = steps > 0.5
        steps  = steps*2 - 1;
        pos    = np.cumsum(steps)
        if np.any(pos == 1):
            nsteps = np.where(pos==1)
        numit += 1

    return nsteps[0][0] + (numit-1)*10000, steps

def maincode():

    numIter = 10000
    numSteps = np.empty([numIter])
    for i in range(0,numIter):
        if i%100 == 0:
            print('Iteration #: ',i)
        numSteps[i],_ = backtrack_steps();


    nsteps_sort,steps_ecdf = bu.ecdf(numSteps)
    plt.loglog(nsteps_sort,1-steps_ecdf)

    # plt.plot(nsteps_sort,steps_ecdf)
    # plt.xscale('log')
    # plt.xlabel('# Steps')
    # plt.ylabel('Cumulative Counts')
    # # plt.hist(numSteps,normed=True)
    plt.show()
