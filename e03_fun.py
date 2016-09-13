import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load Data
wt   = np.loadtxt('data/wt_lac.csv'  ,skiprows=3,delimiter=',')
q18a = np.loadtxt('data/q18a_lac.csv',skiprows=3,delimiter=',')
q18m = np.loadtxt('data/q18m_lac.csv',skiprows=3,delimiter=',')

# Compute Theoretical Curve
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    num  = RK*np.power(1+c/KdA,2)
    den  = np.power(1+c/KdA,2) + Kswitch*np.power(1+c/KdI,2)
    fold = np.power(1 + num/den,-1)

    data = np.zeros([len(fold),2])
    data[:,0] = c
    data[:,1] = fold

    return data

conc_id = np.logspace(-6,2,100)
wt_id   = fold_change(conc_id,141.5)
q18a_id = fold_change(conc_id,16.56)
q18m_id = fold_change(conc_id,1328)

# Compute Fold Change
def fold_change_bohr(bohr_parameter):
    """
    Computes fold change as a function of bohr parameter
    """
    fold = 1/(1 + np.exp(-1*bohr_parameter))
    return fold

# Compute Bohr Parameter as function of concentration
def bohr_from_conc(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Computes bohr change as function of concentration
    """
    data = fold_change(c,RK)
    temp = np.log(data[:,1])
    bohr = np.zeros_like(data)
    bohr[:,0] = data[:,1]
    bohr[:,1] = temp

    return bohr
def plotwrap2():
    wt_br   = bohr_from_conc(wt[:,0],141.5)
    q18a_br = bohr_from_conc(q18a[:,0],16.56)
    q18m_br = bohr_from_conc(q18m[:,0],1328)
    tmp_br  = np.linspace(-6,6,1000)
    foldChBr= fold_change_bohr(tmp_br)

    idealbr = np.zeros([len(tmp_br),2])
    idealbr[:,0] = foldChBr
    idealbr[:,1] = tmp_br

    plt.close()
    plotdata(wt_br  ,color = 'b',mark='*',linestyle='none')
    plotdata(q18a_br,color = 'r',mark='*',linestyle='none')
    plotdata(q18m_br,color = 'g',mark='*',linestyle='none')
    plotdata(idealbr,color = 'k')
    plt.legend(('wt','Q18a','Q18m'),loc='best')
    plt.xlabel('Fold Change')
    plt.ylabel('Bohr')
    plt.show()

# Plot Data
def plotwrap():
    """
    Plots all data types on single axes
    """
    plotdata(wt  ,color = 'b',mark='*',linestyle='none')
    plotdata(q18a,color = 'r',mark='*',linestyle='none')
    plotdata(q18m,color = 'g',mark='*',linestyle='none')
    plotdata(wt_id,  color = 'b')
    plotdata(q18a_id,color ='r')
    plotdata(q18m_id,color = 'g')
    plotlabel()
    plt.legend(('Wt','Q18a','Q18m'),loc='best')
    plt.show()

def plotdata(data,color = 'b',mark = '.',linestyle='-'):
    """
    Plots col 1 vs col2
    """
    data = np.sort(data,0)
    IPTG = data[:,0]
    Fold = data[:,1]

    plt.semilogx(IPTG,Fold,color,marker=mark,linestyle=linestyle)

def plotlabel():
    """
    Adds labels to IPTG(mM) vs Fold Change plot
    """
    plt.xlabel('IPTG (mM)')
    plt.ylabel('Fold Change')
