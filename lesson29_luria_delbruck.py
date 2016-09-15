import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Specify Parameters
n_gen   = 16
# Chance of having beneficial mutation
r       = 1e-5
# Total Number of Cells
n_cells = 2**(n_gen-1)

ai_samples = np.random.binomial(n_cells,r,size=100000)

# print('AI mean:',np.mean(ai_samples))
# print('AI std:',np.std(ai_samples))
# print('Fano factor: ',np.var(ai_samples) / np.mean(ai_samples))
#
# plt.plot(np.bincount(ai_samples) / len(ai_samples), marker='.', markersize=10,
#         linestyle='None')
#
# plt.xlabel('Number of survivors')
# plt.ylabel('Probability')
# plt.xticks(np.arange(ai_samples.max()+1));
# plt.margins(0.02)
# plt.show()


def draw_random_mutation(n_gen,r):
    """Draw sample under random mutation hypothesis"""
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g-2*n_mut,r)

    return n_mut

def sample_random_mutation(n_gen, r, n_samples):
    """Sample out of the Luria-Delbruck distribution"""
    # Initialize samples
    samples = np.empty(n_samples)

    # Draw the samples
    for i in range(n_samples):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

def print_stats(data,desc):
    print(desc,' mean:',np.mean(data))
    print(desc,' std:',np.std(data))
    print('Fano factor: ',np.var(data) / np.mean(data))

rm_samples = sample_random_mutation(n_gen, r, 100000).astype(int)
print_stats(rm_samples,desc='rm')
