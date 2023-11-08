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
    return 2 * x**3 -15 * math.sqrt(x)

# Peform the bisection method
def false_position(xl,xu,loops = 10):
    print()
    xrt = xl
    for i in range(loops):
        xrt_old = xrt
        xrt = xl - f(xl) * (xu-xl)/(f(xu)-f(xl))
        err = abs((xrt - xrt_old)/xrt)*100
        print(f'Iter: {(i+1):2.0f}   x-root: {xrt:.6f}   error: {err:.6f}')
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl = xrt
    return xrt, err

# Set up values for bisection method
x_lower = 2.0
x_upper = 3.0
num_loops = 3

# Check for a good bracket, then call bisection method
if f(x_lower) * f(x_upper) > 0:
    print('\nYour interval does not bracket the root.\n')
else:
    root, error = false_position(x_lower, x_upper, num_loops)
    print(f'\nAfter {num_loops} iterations the final')
    print(f'estimate of the root is {root:.6f}')
    print(f'with a relative error of {error:.6f} %\n')