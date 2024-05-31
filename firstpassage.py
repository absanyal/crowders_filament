import numpy as np
from distributions import firstpassage
import matplotlib.pyplot as plt

first_hit_raw, second_hit_raw = np.loadtxt("hitting_times.txt", unpack=True)

max_t = 120.0
D_input = 0.068

second_hit = []
first_hit = []

for t in second_hit_raw:
    if (t != max_t):
        second_hit.append(t)

print("Number of attachments found: {} out of {}".format(
    len(second_hit), len(second_hit_raw)))
print("{:3.2f} % successfully attached".format(
    100.0 * len(second_hit) / len(second_hit_raw)))

print("Mean first passage time: {}".format(np.mean(second_hit)))
print("Standard deviation: {}".format(np.std(second_hit)))

mean_time = np.mean(second_hit)

bins_list = np.arange(0, max_t, 1.0)
# bins_list = "auto"

plt.figure(tight_layout=True)

plt.axvline(x=mean_time, color='r', linestyle='--', label='Mean time: {:.2f}'.format(mean_time))

plt.hist(second_hit, bins=bins_list, histtype='bar', rwidth=0.8,
         color='b', edgecolor='None', density=True, align='right')

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel("Frequency", fontsize=18)

plt.title('D = {:.4f}'.format(D_input))

plt.xlim(0, max_t)

# Theoretical distribution

theta = 0
theta_rad = np.radians(theta)

t_list = np.linspace(0.1, max_t, 1000)
fp_list = np.zeros(len(t_list))

for i in range(len(t_list)):
    fp_list[i] = D_input * firstpassage(D_input * t_list[i], theta_rad)

plt.plot(t_list, fp_list, label=r'First passage $({}\degree)$'.format(
    theta), linestyle="-", color="r")

plt.legend()

plt.savefig("time_hist.pdf")

plt.clf()
plt.cla()

for t in first_hit_raw:
    if (t != max_t):
        first_hit.append(t)

print("Number of first attachments found: {} out of {}".format(
    len(first_hit), len(first_hit_raw)))

print("{:3.2f} % successfully attached".format(
    100.0 * len(first_hit) / len(first_hit_raw)))

mean_one_linker_time = np.mean(first_hit)

plt.figure(tight_layout=True)

plt.axvline(x=mean_one_linker_time, color='r', linestyle='--', label='Mean time: {:.2f}'.format(mean_one_linker_time))

plt.hist(first_hit, bins=bins_list, histtype='bar', rwidth=0.8,
         color='b', edgecolor='None', density=True, align='right')

plt.plot(t_list, fp_list, label=r'First passage $({}\degree)$'.format(
    theta), linestyle="-", color="r")

plt.xlabel(r"$t/\tau$", fontsize=18)
plt.ylabel("Frequency", fontsize=18)

plt.title('D = {:.4f}'.format(D_input))

plt.xlim(0, max_t)

plt.legend()

plt.savefig("time_hist_first.pdf")
