'''
File: int_equation.py
Author: Bryce Woodland
Date: 12/6/2022
Purpose: Implement the trapezoid method to 
approximate the integral of an equation
'''
import numpy as np

# Define a function that contains the equation
# that we want to find the integral of
def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7
def true_fun(x):
    return ((2*up_limit**4)/4 + (4*up_limit**3)/3 + (5*up_limit**2)/2 + 7*up_limit) - ((2*low_limit**4)/4 + (4*low_limit**3)/3 + (5*low_limit**2)/2 + 7*low_limit)

# Introduce the program to the user
print("\nIntegrating the function in the 'my_fun' function")
print('from {low_limit} to {up_limit} with a step size of {delta} gives the following results:')

# Set up variable values
low_limit = 0
up_limit = 5
delta = 0.2
x = np.arange(low_limit,up_limit+delta,delta)
x_true = np.arange(low_limit,up_limit+delta,delta)
if x[-1] > up_limit:
    x[-1] = up_limit
print(x)

# Approximate the integral using the trapezoidal method
area_total = 0
for i in range(len(x)-1):
    trap_area = (x[i+1] - x[i]) * (my_fun(x[i]) + my_fun(x[i+1]))/2
    area_total += trap_area
    true_int = ((2*up_limit**4)/4 + (4*up_limit**3)/3 + (5*up_limit**2)/2 + 7*up_limit) - ((2*low_limit**4)/4 + (4*low_limit**3)/3 + (5*low_limit**2)/2 + 7*low_limit)
    true_relative_error = abs(true_int - area_total)/true_int*100

# Display the final approximation of the integral
print(f'\nThe value of the integral is {area_total:.3f}')
print(f'True value of the integral: {true_int:.3f}')
print(f'True relative error: {true_relative_error:.3f} %')
print()