import math

# Do you want to calculate area or volume?
calculation = input('Do you want to calculate an AREA or a VOLUME?\n')

# Area
if calculation.lower() == 'area':
    shapearea = input('Do you want to find the area of a TRIANGLE or CIRCLE?\n')

    # Triangle Area
    if shapearea.lower() == 'triangle':
        base = float(input('What is the base of the triangle?\n'))
        height = float(input('What is the height of the triangle?\n'))
        triangle = 1/2*base*height
        print(f'The area of the triangle is {triangle:.2f} units squared.')

        # Circle Area
    elif shapearea.lower() == 'circle':
        radiuscircle = float(input('What is the radius of the circle?\n'))
        circle = math.pi*radiuscircle**2
        print(f'The area of the circle is {circle:.2f} units squared.')

        # Invalid response
    else:
        print('You did not enter a valid option.')

        # Volume
elif calculation.lower() == 'volume':
    shapevol = input('Do you want to find the volume of a SPHERE or CYLINDER?\n')

    # Sphere volume
    if shapevol.lower() == 'sphere':
        radiussphere = float(input('What is the radius of the sphere?\n'))
        sphere = 4/3*math.pi*radiussphere**3
        print(f'The volume of the sphere is {sphere:.2f} units cubed.')

        # Cylinder Volume
    elif shapevol.lower() == 'cylinder':
        radiuscyl = float(input('What is the radius of the cylinder?\n'))
        length = float(input('What is the length of the cylinder?\n'))
        cylinder = math.pi*radiuscyl**2*length
        print(f'The volume of the cylinder is {cylinder:.2f} units cubed.')

        # Invalid response
    else:
        print('You did not enter a valid option.')
else:
    print('You did not enter a valid option.')
