import numpy as np
import pandas as pd
import bootcamp_utils as bu
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def dict_from_list(list1,list2):
    """Creates dict from list; list1 contains keys"""
    mydict = {}
    for val1, val2 in zip(list1,list2):
        mydict[val1] = val2

    return mydict

# Load data
d1973 = pd.read_csv('data/grant_1973.csv',comment='#')
d1975 = pd.read_csv('data/grant_1975.csv',comment='#')
d1987 = pd.read_csv('data/grant_1987.csv',comment='#')
d1991 = pd.read_csv('data/grant_1991.csv',comment='#')
d2012 = pd.read_csv('data/grant_2012.csv',comment='#')

# Reformat d1973
d1973 = d1973.rename(columns={'yearband':'year'})
d1973['year'] = d1973['year']+1900;

# Add year columns to the remaining data sets
d1975['year'] = 1975
d1987['year'] = 1987
d1991['year'] = 1991
d2012['year'] = 2012

# Fix column names for 1991, 2012 data sets
colnames1 = ['band','species','bk length (mm)','bk depth (mm)','year']
colnames2 = ['band','species','year','bk length (mm)','bk depth (mm)']
d1973     = d1973.rename(columns=dict_from_list(list(d1973.columns),colnames2))
d1975     = d1975.rename(columns=dict_from_list(list(d1987.columns),colnames1))
d1987     = d1987.rename(columns=dict_from_list(list(d1987.columns),colnames1))
d1991     = d1991.rename(columns=dict_from_list(list(d1991.columns),colnames1))
d2012     = d2012.rename(columns=dict_from_list(list(d2012.columns),colnames1))

dall  = pd.concat([d1973,d1975,d1987,d1991,d2012],ignore_index=True)
dall1 = dall.drop_duplicates(subset='band')
d1987_bk = dall1.loc[ dall1['year']==1987,['bk depth (mm)','bk length (mm)','species']]

# x_sc_dep,y_sc_dep = bu.ecdf(d1987_bk.loc[d1987_bk['species']=='scandens','bk depth (mm)'])
# x_ft_dep,y_ft_dep = bu.ecdf(d1987_bk.loc[d1987_bk['species']=='fortis','bk depth (mm)'])
# x_sc_len,y_sc_len = bu.ecdf(d1987_bk.loc[d1987_bk['species']=='scandens','bk length (mm)'])
# x_ft_len,y_ft_len = bu.ecdf(d1987_bk.loc[d1987_bk['species']=='fortis','bk length (mm)'])

# plt.figure(1)
# plt.plot(x_sc_dep,y_sc_dep)
# plt.plot(x_ft_dep,y_ft_dep)
# plt.xlabel('Beak Depth (mm)')
# plt.legend({'Scandens','Fortis'})
#
# plt.figure(2)
# plt.plot(x_sc_len,y_sc_len)
# plt.plot(x_ft_len,y_ft_len)
# plt.xlabel('Beak Length (mm)')
# plt.legend({'Scandens','Fortis'})

# plt.figure(3)
# ax = d1987_bk.loc[d1987_bk['species']=='scandens',:].plot(x='bk depth (mm)', y='bk length (mm)', kind='scatter')
# d1987_bk.loc[d1987_bk['species']=='fortis',:].plot(x='bk depth (mm)', y='bk length (mm)', kind='scatter',ax=ax,color='g')
# plt.title('Comparison for 1987')
# ax1 = dall1.loc[ (dall1['species']=='scandens') & (dall1['year']==1973),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter')
# dall1.loc[       (dall1['species']=='fortis')   & (dall1['year']==1973),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter',ax=ax1,color='g')
# plt.title('Comparison for 1973')
# ax2 = dall1.loc[ (dall1['species']=='scandens') & (dall1['year']==1975),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter')
# dall1.loc[       (dall1['species']=='fortis')   & (dall1['year']==1975),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter',ax=ax2,color='g')
# plt.title('Comparison for 1975')
# ax3 = dall1.loc[ (dall1['species']=='scandens') & (dall1['year']==1991),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter')
# dall1.loc[       (dall1['species']=='fortis')   & (dall1['year']==1991),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter',ax=ax3,color='g')
# plt.title('Comparison for 1991')
# ax4 = dall1.loc[ (dall1['species']=='scandens') & (dall1['year']==2012),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter')
# dall1.loc[       (dall1['species']=='fortis')   & (dall1['year']==2012),:].plot(x='bk depth (mm)',y='bk length (mm)',kind='scatter',ax=ax4,color='g')
# plt.title('Comparison for 2012')



plt.show()
