import numpy as np
import pandas as pd
import bootcamp_utils as bu
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# data = pd.read_csv('data/bee_weight.csv',comment='#')
#
# x_cont,y_cont = bu.ecdf(data.loc[data['Treatment']=='Control','Weight'])
# x_pest,y_pest = bu.ecdf(data.loc[data['Treatment']=='Pesticide','Weight'])
#
# grp1 = data.loc[:,['Weight','Treatment']].groupby('Treatment')
# means = grp1.apply(np.mean)
# print(means)
#
# reps_cont,ci_cont = bu.draw_bs_reps(x_cont,sz = 10000)
# reps_pest,ci_pest = bu.draw_bs_reps(x_pest,sz = 10000)
#
# print(ci_cont)
# print(ci_pest)

data = pd.read_csv('data/bee_sperm.csv',comment='#')

x_cont,y_cont = bu.ecdf(data.loc[data['Treatment']=='Control','Quality'].dropna())
x_pest,y_pest = bu.ecdf(data.loc[data['Treatment']=='Pesticide','Quality'].dropna())

grp1 = data.loc[:,['Treatment','Quality']].groupby('Treatment')
means = grp1.apply(np.mean)
print(means)

reps_cont,ci_cont = bu.draw_bs_reps(x_cont,func=np.median,sz = 10000)
reps_pest,ci_pest = bu.draw_bs_reps(x_pest,func=np.median,sz = 10000)

print('Control:', ci_cont)
print('Pesticide:',ci_pest)
