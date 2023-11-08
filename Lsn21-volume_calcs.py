from cmath import pi
# Calculate the volume of either a cylinder or a sphere

shape = input('Do you want to find the volume of a SPHERE or CYLINDER?')
if shape.lower() == 'sphere':
    radius_sphere = float(input('What is the radius of the sphere?'))
    sphere_volume = 4/3*pi*radius_sphere**3
    print()
    print(f'The volume of the sphere is {sphere_volume:.2f} units cubed.')
elif shape.lower() == 'cylinder':
    radius_cylinder = float(input('What is the radius of the cylinder?'))
    length = float(input('What is the length of the cylinder?'))
    cylinder_volume = pi*radius_cylinder**2*length
    print()
    print(f'The volume of the cylinder is {cylinder_volume:.2f} units cubed.')
else:
    print()
    print('You did not enter a valid option.')
print()
