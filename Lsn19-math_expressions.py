""""
File: math_expressions_demo.py
Author: Bryce Woodland
Date: 10/27/22
Purpose: Evaluate a math expression and to calculate
the area of a circle
"""
import math

# Evaluate the math expression and display the result

y=3/(2-math.sqrt(7))-6*4+2**2
print(f'\nThe value of the expression is {y:.3f}\n')

# Prompt the user for the radius of the circle
radius = input('What is the radius of the circle? ')

# Calculate the area of the circle and display the result
area = math.pi*float(radius)**2
print(f'The area of the circle is {area:.3f}')
print()
