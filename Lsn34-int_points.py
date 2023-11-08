'''
File: int_equation.py
Author: Bryce Woodland
Date: 12/6/2022
Purpose: Implement the trapezoid method to 
approximate the integral of discrete points
'''
import numpy as np

# Introduce the program to the user
print('\nThis program approximates the integrals')
print('using discrete data points. \n')

# Set up variable values
time = [0,1,2.5,3,4.5,6]
velocity = [0,1,1.5,2,3,4]

# Display values to user
print(f'The time values are {time}')
print(f'The velocity values are {velocity}')

# Approximate the integral using the trapezoidal method
area_total = 0
for i in range(len(time)-1):
    trap_area = (time[i+1] - time[i]) * (velocity[i] + velocity[i+1])/2
    area_total += trap_area

# Display the final approximation of the integral
print(f'The value of the integral is {area_total:.2f}')
print()