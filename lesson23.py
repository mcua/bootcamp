import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load Data
data_txt = np.loadtxt('data/collins_switch.csv',delimiter=',',skiprows=2)
xa_high  = np.loadtxt('data/xa_high_food.csv')
xa_low   = np.loadtxt('data/xa_low_food.csv')

iptg = data_txt[:,0]
gfp  = data_txt[:,1]
sem  = data_txt[:,2]

# plt.semilogx(iptg,gfp,linestyle = 'none',marker='.',markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')

# plt.errorbar(iptg,gfp,yerr=sem,linestyle='none',marker='.',markersize=10)
# plt.xscale('log')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.show()

# Functions
def ecdf(data):

    x = np.sort(data)
    y = np.arange(1,len(x)+1)/len(x)

    return np.column_stack((x,y))

def plotwrp_ecdf():
    ecdf_high = ecdf(xa_high)
    ecdf_low  = ecdf(xa_low)

    plt.plot(ecdf_high[:,0],ecdf_high[:,1],marker='.',linestyle ='none',alpha=0.5,markersize=10)
    plt.plot(ecdf_low[:,0],ecdf_low[:,1],marker='.',linestyle ='none',alpha=0.5,markersize=10)
    plt.ylabel('ECDF')
    plt.xlabel('Cross Sectional Area ($\mu$m)')
    plt.legend(('high','low'),loc='best',fontsize=14)
    plt.show()
