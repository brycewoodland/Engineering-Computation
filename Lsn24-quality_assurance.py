import math
import numpy as np
print()
length1 = np.array([12, 10.59, 10.7, 10.58, 10.55, 10.57, 10.63, 10.45, 10.58, 10.47])
length2 = np.array([3.15, 3.27, 3.3, 3.18, 3.23, 3.33, 3.25, 3.27, 3.18, 3.19])
large_diam = np.array([1.01, .97, 1, 1.06, 1.05, .93, 1.02, 1.11, .92, .93])
small_diam = np.array([.53, .47, .47, .46, .5, .51, .49, .46, .45, .51])

volume = math.pi*(large_diam*0.5)**2*(length1-length2)+math.pi*(small_diam*0.5)**2*length2
print(f'The volume values are {volume}. ')
print(f'The average of the volumes is {volume.mean():.2f}. ')
print(f'The standard deviation of the volumes is {volume.std():.2f}. ')
print(f'The maximum of the volumes is {volume.max():.2f}. ')
print(f'The minimum of the volumes is {volume.min():.2f}. ')
print()
