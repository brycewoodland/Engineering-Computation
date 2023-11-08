'''
File: Bisect_demo.py
Author: Bryce Woodland
Date: 11/30/2022
Purpose: Use the false position method to find
the root of an equation
'''
import math

# define the function
def f(x):
    return 2 * x**2 -9.5 * math.sqrt(x)

# Peform the bisection method
def false_position(xl, xu, error_tol):
    print()
    counter = 0
    error = 1
    xrt = xl
    while error > error_tol:
        xrt_old = xrt
        counter += 1
        xrt = xl - f(xl) * (xu-xl)/(f(xu)-f(xl))
        error = abs((xrt - xrt_old)/xrt)*100
        print(f'Iter: {(counter):2.0f}   x-root: {xrt:.6f}   error: {error:.6f}')
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl = xrt
    return xrt, error, counter

# Set up values for bisection method
x_lower = 2.5
x_upper = 3.0
error_tol = 0.001

# Check for a good bracket, then call bisection method
if f(x_lower) * f(x_upper) > 0:
    print('\nYour interval does not bracket the root.\n')
else:
    root, error, counter = false_position(x_lower, x_upper, error_tol)
    print(f'\nAfter {counter} iterations the final')
    print(f'estimate of the root is {root:.6f}')
    print(f'with a relative error of {error:.6f} %\n')