import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Compute rabbit and fox simulation

# Parameters
alpha = 1
beta  = 0.2
delta = 0.3
gamma = 0.8
Dt    = 0.01
ts    = [0,60]
init  = [10,1]

# Functions
def simulate_foxrabbit(ts=[0,60],Dt=0.01,init=[10,1]):
    t = np.arange(ts[0],ts[1],Dt)

    rab = np.empty_like(t)
    fox = np.empty_like(t)

    rab[0] = init[0]
    fox[0] = init[1]

    for i in range(1,len(t)):
        rab[i] = rab[i-1] + Dt*(alpha*rab[i-1]-beta*fox[i-1]*rab[i-1])
        fox[i] = fox[i-1] + Dt*(delta*fox[i-1]*rab[i-1] - gamma*fox[i-1])

    res = np.empty([len(t),2])
    res[:,0] = rab
    res[:,1] = fox

    plt.plot(t,res[:,0],t,res[:,1])
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend(('Rabbit','Fox'))
    return res
