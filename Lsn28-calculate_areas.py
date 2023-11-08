"""
File: areas_demo.py
Author: Bryce Woodland
Date: 6/28/22
Purpose: Create functions to calculate the area of basic shapes
"""
import math

# function to compute the area of a square
def compute_area_square(length):
    area_square = length**2
    return area_square

# function to compute the area of a rectangle
def compute_area_rectangle(length1, length2):
    area_rectangle = length1 * length2
    return area_rectangle

# function to compute the area of a circle
def compute_area_circle(radius):
    area_circle = math.pi * radius**2
    return area_circle

print()  
shape = input("What shape do you want the area of ('square', 'rectangle', 'circle'? " ).lower()
if shape == 'square':
    length = float(input('What is the length of the side of the square? '))
    area = compute_area_square(length)
    print(f'The area of the square is {area:.2f}\n')
elif shape == 'rectangle':
    length1 = float(input('What is the length of the first side of the rectangle? '))
    length2 = float(input('What is the length of the second side of the rectangle? '))
    area = compute_area_rectangle(length1,length2)
    print(f'The area of the rectangle is {area:.2f}\n')
elif shape == 'circle':
    radius = float(input('What is the radius of the circle? '))
    area = compute_area_circle(radius)
    print(f'The area of the circle is {area:.2f}\n')
else:
    print('Invalid Entry\n')
