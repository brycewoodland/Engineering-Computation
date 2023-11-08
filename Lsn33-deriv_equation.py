'''
File: deriv_function_demo.py
Author: Bryce Woodland
Date: 12/4/2022
Purpoese: Approximate the derivative of a function
at a single point or across many points
'''

import numpy as np
import matplotlib.pyplot as plt

# define the function with the equation
def fun(x):
    return 2*x**3 +4*x**2 + 5*x +7

# Define the divided difference approximations
def forward(xi, xi_plus):
    return (fun(xi_plus) - fun(xi))/(xi_plus - xi)

def backward(xi, xi_minus):
    return (fun(xi) - fun(xi_minus))/(xi - xi_minus)

def centered(xi_plus, xi_minus):
    return(fun(xi_plus)-fun(xi_minus))/(xi_plus - xi_minus)

# Approximate the derivative at a point
xi = 3.5
dx = 0.5
slope_forward = forward(xi, xi+dx)
slope_backward = backward(xi, xi-dx)
slope_centered = centered(xi+dx, xi-dx)

# Print results
print('\nThe forward difference approximation of the')
print(f'slope of the function at x = {xi} is {slope_forward}')
print('\nThe backward difference approximation of the')
print(f'slope of the function at x = {xi} is {slope_backward}')
print('\nThe centered difference approximation of the')
print(f'slope of the function at x = {xi} is {slope_centered}')
print()

# Approximate the derivative across a series of points
x = np.arange(0,5.1,0.1)
y = fun(x)

deriv = []
for i in range(len(x)):
    if i == 0:
        deriv.append(forward(x[i], x[i+1]))
    elif i == len(x)-1:
        deriv.append(backward(x[i], x[i-1]))
    else: 
        deriv.append(centered(x[i+1], x[i-1]))

# Print results
print("\n x     f(x)     f'(x)")
for i in range(len(x)):
    print(f'{x[i]:3.1f} {y[i]:8.3f} {deriv[i]:7.2f}')

# Plot results
plt.plot(x,y, label = 'Equation f(x)')
plt.grid(True)
plt.plot(x,deriv, label = "Derivative f'(x)")
plt.legend(loc = "lower right")
plt.xlabel('x')
plt.title('Plot of Equation and Derivative')
plt.xlim(0,6)
plt.ylim(0,450)
plt.show()
