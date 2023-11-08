'''
File: linear_equations_tool.py
Author: Bryce Woodland
Date: 12/2/2022
Purpose: solve various matrices
'''

# Solve a system of linear equations
import numpy as np

# Display message to the user
print('\nWelcome to the Linear Equations Tool!\n')

# Get input from the user
num_eq = int(input('How many equations and how many unknowns are there? '))

# Initialize matrices
A = np.zeros((num_eq, num_eq))
b = np.zeros(num_eq)

# Build the A matrix
for row in range(num_eq):
    print(f'\n[A] matrix values for row {row+1}')
    for column in range(num_eq):
        A[row,column] = float(input(f'Column {column+1}: '))
print()

# Check to see if the A matrix is singular
if np.linalg.det(A) == 0:
    print('\nThe A matrix is singular so')
    print('the system cannot be solved!\n')
else:
    for row in range(num_eq):
        b[row] = float(input(f'[b] Vector values for row {row+1}: '))

    x = np.linalg.solve(A,b)

    #Display the results
    print(f'\nA Matrix: \n{A}')
    print(f'\nb Vector: \n{b}')
    print('\nx Values:')
    for i in range(len(x)):
        print(f'x{i+1} = {x[i]:.3f}')
