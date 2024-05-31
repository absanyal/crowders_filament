import numpy as np
import matplotlib.pyplot as plt

first_hit_raw, second_hit_raw = np.loadtxt("hitting_times.txt", unpack=True)

max_t = 120.0

first_hit = []
second_hit = []

diff = []

for t_i in range(len(first_hit_raw)):
    if first_hit_raw[t_i] != max_t and second_hit_raw[t_i] != max_t:
                diff.append(second_hit_raw[t_i] - first_hit_raw[t_i])

bins_list = np.arange(0, max_t, 1.0)

plt.figure(tight_layout=True)
plt.hist(diff, bins=bins_list, histtype='bar', rwidth=0.8, edgecolor='None', density=True, color='b')

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel("Frequency", fontsize=18)

#plt.yscale('log')

plt.savefig("hitting_diff.pdf")
