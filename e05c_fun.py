import numpy as np
import pandas as pd
import bootcamp_utils as bu
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def lin_fit(x,A,b):
    return A*x + b

# Load data
dall  = pd.read_csv('data/grant_complete.csv',comment='#')

def main_5c():
    yrs   = list(dall['year'].drop_duplicates())
    specs = list(dall['species'].drop_duplicates())
    slope = []
    # Process Each Files
    with sns.axes_style('dark'):
        fig, ax = plt.subplots(len(yrs), len(specs))
        for y,yr in enumerate(yrs):
            for s,spec in enumerate(specs):
                dtmp = dall.loc[(dall['year']==yr) & (dall['species']==spec),:]
                bkdepth  = dtmp['beak depth (mm)']
                bklength = dtmp['beak length (mm)']
                A    = 1
                b    = 0
                p0   = [A,b]
                p, _ = scipy.optimize.curve_fit(lin_fit,bklength,bkdepth, p0=p0)
                yfit = lin_fit(bklength,*tuple(p))

                ax[y,s].plot(bklength,bkdepth,marker='.',linestyle='none')
                ax[y,s].plot(bklength,yfit,color='gray')
                ax[y,s].set_title(str(yr) + '; ' + spec)
                # ax[y,s].xlabel('Beak Length (mm)')
                # ax[y,s].ylabel('Beak Depth (mm)')

                slope.append(p)
    fig.tight_layout()
    plt.show()
    return slope
