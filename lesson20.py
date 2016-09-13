import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Test Data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low  = np.loadtxt('data/xa_low_food.csv')

x      = np.linspace(-15,15,400)
norm_I = 4*(scipy.special.j1(x)/x)**2

# plt.close()
# plt.plot(x,norm_I,marker='.',linestyle='none')
# plt.xlabel('$x$')
# plt.ylabel('$I(x)/I_0$')
# plt.margins(0.02)
# plt.show()

# Array Generation
# A = np.array([[6.7, 1.3, 0.6, 0.7],
#               [0.1, 5.5, 0.4, 2.4],
#               [1.1, 0.8, 4.5, 1.7],
#               [0.0, 1.5, 3.4, 7.5]])
#
# b = np.array( [1.1, 2.3, 3.3, 3.9])

# Processing Spike Data
data = np.loadtxt('data/retina_spikes.csv',delimiter=',',skiprows=2)
t    = data[:,0]
volt = data[:,1]

plt.close()
plt.plot(t,volt);
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')
plt.xlim(1395,1400)
plt.show()

# Functions
def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """

    # Compute diameter from area
    diameter = 2*np.sqrt(xa/np.pi)

    return diameter

def easy_reshape(arr,ncols,order='C'):
    """
    Guarantee that reshaping works by defining only one shape parameter.
    """
    outArr = np.reshape(arr,[ncols,len(arr)/ncols],order)
    return outArr

def plotwrap_xa():
    low_min  = np.min(xa_low)
    low_max  = np.max(xa_low)
    high_min = np.min(xa_high)
    high_max = np.max(xa_high)
    glob_min = ( np.min([low_min,high_min])//50)*50
    glob_max = ( np.max([low_max,high_max])//50)*50
    bins = np.arange(glob_min-50,glob_max+100,50)
    _ = plt.hist(xa_low , normed=True, bins=bins)
    _ = plt.hist(xa_high, normed=True, bins=bins, alpha=0.5)
    plt.xlabel('Cross-sectional area (µm$^2$)')
    plt.ylabel('Frequency')
    plt.legend(('Low','High'))
    plt.savefig('tempfig.pdf',bbox_inches ='tight')
    plt.show()
