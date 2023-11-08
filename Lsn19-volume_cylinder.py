from cmath import pi
import math


radius = input('What is the radius of the cylinder? \n')
length = input('What is the length of the cylinder? \n')
volume = pi*float(radius)**2*float(length)
print(f'\n 2.The volume of the cylinder is {volume:.3f} units cubed.\n')
