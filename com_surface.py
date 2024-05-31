import numpy as np
from block import block, distance_from_axis, distance_from_surface
import matplotlib.pyplot as plt

xlo = 0
xhi = 1000
ylo = 0
yhi = 350
zlo = 0
zhi = 350

b = block(xlo, xhi, ylo, yhi, zlo, zhi)

n_atoms, n_linkers, n_link_skip = np.loadtxt('info.txt')

runmax = 1050

plt.figure(tight_layout=True)

t = np.loadtxt('com_pos/com_pos.1.txt', usecols=(0,))

dsx2_cumu = np.zeros(len(t))
dsy2_cumu = np.zeros(len(t))
dsz2_cumu = np.zeros(len(t))

for run_i_m1 in range(0, runmax):

    plt.clf()
    plt.cla()

    run_i = run_i_m1 + 1
    # print("="*50)
    print("Processing run {}".format(run_i))

    t, cmx, cmy, cmz = np.loadtxt(
        'com_pos/com_pos.{}.txt'.format(run_i), unpack=True)
    
    dsx = np.zeros(len(t))
    dsy = np.zeros(len(t))
    dsz = np.zeros(len(t))
    
    for t_i in range(len(t)):
        rP = [cmx[t_i], cmy[t_i], cmz[t_i]]
        dx, dy, dz = distance_from_surface(b, rP)
        dsx[t_i] = dx
        dsy[t_i] = dy
        dsz[t_i] = dz
        
    dsx2 = dsx**2
    dsy2 = dsy**2
    dsz2 = dsz**2
    
    dsx2_cumu += dsx2
    dsy2_cumu += dsy2
    dsz2_cumu += dsz2

    plt.plot(t, dsy, linewidth=1.0, label=r"$s$", color='black')
    plt.xlabel(r'$t/\tau$', fontsize=18)
    plt.ylabel(r'$\Delta s$', fontsize=18)
    plt.xlim(left=0.0)
    plt.ylim(bottom=0.0)
    plt.legend(fontsize=19)
    plt.savefig('s_disp.{}.pdf'.format(run_i))

plt.clf()
plt.cla()

dsx2_cumu /= runmax
dsy2_cumu /= runmax
dsz2_cumu /= runmax

with open('s_disp_avg.txt', 'w') as f:
    for i in range(len(t)):
        f.write('{} {}\n'.format(t[i], dsy2_cumu[i]))