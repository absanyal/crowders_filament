import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def f(x, m, c):
    return m * x + c

t, x, y, z = np.loadtxt('com_pos/com_pos.1.txt', unpack=True)

t, dtheta = np.loadtxt('ang_deviation.1.txt', unpack=True)

t_max = len(t)
sample_window_fraction = 0.1
sample_window = int(t_max * sample_window_fraction)
print("Total iterations: {}".format(t_max))
print("Sample window: {} iterations".format(sample_window))