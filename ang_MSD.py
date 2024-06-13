import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

n_atoms, n_linkers, n_link_skip = np.loadtxt('info.txt')

def f(x, a, b):
    return a*x + b

dimension = 3

runmax = 1

t = np.loadtxt('e2e_pos/e2e_pos.1.txt', usecols=(0,))

dtheta2_cumu = np.zeros(len(t))

for run_i_m1 in range(0, runmax):
    
    run_i = run_i_m1 + 1
    
    print("Processing run {}".format(run_i))
    
    t, theta = np.loadtxt('ang_deviation.{}.txt'.format(run_i), unpack=True, usecols=(0, 1))
    
    theta0 = theta[0]
    
    dtheta = theta - theta0
    dtheta2 = dtheta**2
    dtheta2_cumu += dtheta2

dtheta2_cumu /= runmax

with open('ang_disp_avg.txt', 'w') as file:
    file.write('# t\tdtheta2\n')
    for i in range(len(t)):
        file.write('{}\t{}\n'.format(t[i], dtheta2_cumu[i]))

plt.plot(t, dtheta2_cumu, linewidth=1.0, label="Angular deviation", color='black')

p_opt, p_cov = curve_fit(f, t, dtheta2_cumu)
Drot = p_opt[0] / (2*dimension)

print("Drot = {:.4f}".format(Drot))

fit = f(t, *p_opt)

plt.plot(t, fit, label = "Linear fit", linewidth=1.0, color='red', linestyle='--')

plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel(r'$\langle \Delta \theta^2 \rangle$', fontsize=18)
plt.xlim(left = 0.0)
plt.ylim(bottom = 0.0)

plt.title(r'$D_{{rot}} = {:.4f}$'.format(Drot), fontsize=18)

plt.legend(fontsize=19)

plt.savefig('ang_MSD.pdf')

