import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
# df_low  = pd.read_csv('data/xa_low_food.csv',  comment='#', header=None)
#
# # Change column headings and concatenate
# df_low.columns  = ['low']
# df_high.columns = ['high']
# df = pd.concat((df_low, df_high), axis=1)

# # Soccer Stuff
# wc_dict = {'Klose': 16,
#            'Ronaldo': 15,
#            'Müller': 14,
#            'Fontaine': 13,
#            'Pelé': 12,
#            'Koscis': 11,
#            'Klinsmann': 11}
# nation_dict = {'Klose': 'Germany',
#                'Ronaldo': 'Brazil',
#                'Müller': 'Germany',
#                'Fontaine': 'France',
#                'Pelé': 'Brazil',
#                'Koscis': 'Hungary',
#                'Klinsmann': 'Germany'}
# s_nation = pd.Series(nation_dict)
# s_goals = pd.Series(wc_dict)
#
# # Create data frame
# df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
