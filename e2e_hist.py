import numpy as np
import matplotlib.pyplot as plt

t, e1x, e1y, e1z, e2x, e2y, e2z = np.loadtxt('e2e_pos/e2e_pos.1.txt', unpack=True)

distance = np.sqrt((e1x - e2x)**2 + (e1y - e2y)**2 + (e1z - e2z)**2)

plt.hist(distance, bins=100, edgecolor = 'None', color='blue', rwidth=0.9)
plt.xlabel('Distance (m)')
plt.ylabel('Frequency')
plt.title('End-to-End Distance')

plt.show()