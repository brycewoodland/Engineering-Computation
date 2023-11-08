'''
File: linear_equations2.py
Author: Bryce Woodland
Date: 12/1/2022
Purpose: solve a linear system of equations'''

import numpy as np

# # 2 by 2 matrix
# A = np.array([[1,-6],[4,12]])
# b = np.array([5,7])

# 3 by 3 matrix
A = np.array([[3,-2,1],[4,0,-6],[1,3,-2]])
b = np.array([-5,-1,-9])

# # 4 by 4 matrix
# A = np.array([[1,2,5,-4],[0,3,7,7],[1,4,-3,2],[4,2,0,1]])
# b = np.array([7,-10,4,2])

# # 5 by 5 matrix
# A = np.array([[1,1,-1,0,1],[0,-1,0,1,-1],[-100,0,-300,0,0],[0,0,-300,-400,0],[0,200,0,0,0]])
# b = np.array([0,0,-10,-50,-20])

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