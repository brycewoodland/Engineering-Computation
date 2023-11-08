'''
File: linear_equations2.py
Author: Bryce Woodland
Date: 12/1/2022
Purpose: solve a linear system of equations'''

import numpy as np

# Define matrices
# A = np.array([[5,2],[4,-3]])
# b = np.array([8,1])
A = np.array([[2,-7,4],[3,1,4],[9,0,-6]])
b = np.array([12,5,-2])

if np.linalg.det(A) == 0:
    print('\nThe A matrix is singular so')
    print('the system cannot be solved!\n')
else:
    x = np.linalg.solve(A,b)

    # Print results
    print(f'\nA Matrix\n{A}')
    print(f'\nb Vector\n{b}')
    print()
    for i in range(len(x)):
        print(f'x{i+1} = {x[i]:.3f}')
    print()
