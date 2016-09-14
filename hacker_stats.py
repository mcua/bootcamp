import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    """
    Computes ECDF of provided data
    """
    x = np.sort(data)
    y = np.arange(1,len(x)+1)/len(x)

    return x,y

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Compute Bootstrap
# n_reps = 100000
# bs_reps_1975 = np.empty(n_reps)
# bs_reps_2012 = np.empty(n_reps)
#
# # Compute replicates
# for i in range(n_reps):
#     bs_sample = np.random.choice(bd_1975, size=len(bd_1975))
#     bs_reps_1975[i] = np.mean(bs_sample)
#     bs_sample = np.random.choice(bd_2012, size=len(bd_2012))
#     bs_reps_2012[i] = np.mean(bs_sample)
#
# # mn_1975 = np.mean(bd_1975)
# # st_1975 = np.std(bd_1975)
# # mn_2012 = np.mean(bd_2012)
# # st_2012 = np.std(bd_2012)
# conf_int_1975 = np.percentile(bs_reps_1975, [2.5, 97.5])
# conf_int_2012 = np.percentile(bs_reps_2012, [2.5, 97.5])
#
# print(conf_int_1975)
# print(conf_int_2012)

def draw_bs_reps(data, func=np.mean, sz = 100):
    reps = np.empty([sz,1])
    for i in range(0,sz):
        bs_samp = np.random.choice(data,size=len(data))
        reps[i] = func(bs_samp)

    conf_int = np.percentile(reps,[2.5,97.5])
    return reps,conf_int

# x_1975   ,y_1975    = ecdf(bd_1975)
# x_2012   ,y_2012    = ecdf(bd_2012)
# x_1975_bu,y_1975_bu = ecdf(bs_sample)
#
# plt.plot(x_1975,y_1975,marker ='.',linestyle='none')
# plt.plot(x_1975_bu,y_1975_bu,marker='.',linestyle='none',alpha=0.5)
# # plt.plot(x_2012,y_2012,marker ='.',linestyle='none')
# plt.xlabel('Beak Depth (mm)')
# plt.ylabel('ECDF')
# plt.show()
