import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x, a, b):
    return a * (1 - x) + b

phi, D = np.loadtxt("D_vs_phi.txt", unpack=True)

phi_min = min(phi)
phi_max = max(phi)

phi_for_plot = np.linspace(phi_min, phi_max, 1000)

D0 = D[0]

D_list = [D0 * (1 - phi_i) for phi_i in phi_for_plot]

plt.plot(phi, D, "-o", label="Data")
plt.plot(phi_for_plot, D_list, label=r"$D_{0}\,(1 - \phi)$")

plt.xlabel(r"$\phi$")
plt.ylabel(r"$D$")

p_opt, p_cov = curve_fit(f, phi, D)
a, b = p_opt

plt.plot(phi_for_plot, f(phi_for_plot, a, b), label="Fit")

plt.legend()

plt.show()