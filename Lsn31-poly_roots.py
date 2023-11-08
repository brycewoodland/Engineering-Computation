import numpy as np
import matplotlib.pyplot as plt

# Plot a polynomial
# coef = [6,-8,4]
# x = np.linspace(-10,10,100)
# y = np.polyval(coef,x)
# plt.plot(x,y)
# plt.grid(True)
# plt.show()

# Find the roots of a polynomial
# my_roots = np.roots(coef)
# print(f'\nA polynomial with coeficients of {coef}')
# print(f'has roots {my_roots}\n')

# Higher-order polynomial
coef = [3,1,-5,0,1,2]
my_roots = np.roots(coef)
print(f'\nA polynomial with coeficients of {coef}')
print('has roots')
for i in range(len(my_roots)):
    print(f'{my_roots[i]:15.3f}')
