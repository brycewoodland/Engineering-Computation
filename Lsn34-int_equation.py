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
    return 3*x**2 + 2*x + 1

# Introduce the program to the user
print('\nThis program approximates the integral of the')
print("equation that is stored in the 'my_fun function'. \n")

# Set up variable values
low_limit = 0
up_limit = 4
delta = 2.0
x = np.arange(low_limit,up_limit+delta,delta)
if x[-1] > up_limit:
    x[-1] = up_limit
print(x)

# Approximate the integral using the trapezoidal method
area_total = 0
for i in range(len(x)-1):
    trap_area = (x[i+1] - x[i]) * (my_fun(x[i]) + my_fun(x[i+1]))/2
    area_total += trap_area

# Display the final approximation of the integral
print(f'The value of the integral is {area_total:.3f}')
print()

