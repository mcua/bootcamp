import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize

def gradient_model(x,I_o,a,lam):
    """Model for Bcd gradient: exponential decya plus backgroun."""
    # assert np.all(np.array(x)>=0)
    if np.any(np.array(x)<0):
        raise RuntimeError('x >= 0')

    # assert np.all(np.array([I_o,a,lam]>=0)
    if np.any(np.array([I_o,a,lam])<0):
        raise RuntimeError('all params must be positive')

    return a + I_o*np.exp(-x/lam)

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x',
                        '[bcd] (a.u.)': 'I_bcd'})

def main():
    p0 = [0.7,0.2,0.25] #I_o,a,lambda
    pOpt,pcov = scipy.optimize.curve_fit(gradient_model,df['x'],df['I_bcd'],p0=p0)

    x_sm = np.linspace(0,1,200)
    I_sm = gradient_model(x_sm,*tuple(pOpt))
    # # Plot experimental Bcd gradient.
    plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')
    plt.plot(x_sm,I_sm,color = 'gray')
    # Label axes (no units on x because it's dimensionless)
    plt.xlabel('x')
    plt.ylabel('I (a.u.)')
    plt.show()
