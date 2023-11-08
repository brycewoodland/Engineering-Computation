"""
File: force_calculator.py
Author: Bryce Woodland
Date: 11/13/2022
"""
import math

print('You may do one of the following:')
print('    1. Break a force into its x and y component forces')
print('    2. Combine component forces into a resultant force and angle')
print('    3. Add multiple forces')
option = int(input('Which option do you want? '))

if option == 1:
    # Get input from the user
    force = float(input('What is the magnitude of the force (in lbs)? '))
    angle = float(input('What is the angle of the force (in degrees)? '))

# Calculate x and y component forces
    fx = force * math.cos(math.radians(angle))
    fy = force * math.sin(math.radians(angle))

# Display results
    print()
    print(f'The x-component of the force is {fx:.1f} lbs.')
    print(f'The y-component of the force is {fy:.1f} lbs.')
    print()

elif option == 2:
    # Get input from the user
    print()
    fx = float(input('What is the x-component of the force (in lbs)? '))
    fy = float(input('What is the y-component of the force (in lbs)? '))
    force = math.sqrt(fx**2+fy**2)

    if fx > 0 and fy > 0:
            angle = math.degrees(math.atan(fy/fx))
    elif fx < 0 and fy >0:
            angle = math.degrees(math.atan(fy/fx)) + 180
    elif fx < 0 and fy < 0:
            angle = math.degrees(math.atan(fy/fx)) + 180
    elif fx > 0 and fy < 0:
            angle = math.degrees(math.atan(fy/fx)) + 360
    elif fx == 0 and fy > 0:
            angle = 90
    elif fx == 0 and fy < 0:
            angle = 270
    elif fx > 0 and fy == 0:
            angle = 0
    else:
            angle = 180

    print()
    print(f'The magnitude of the force is {force:.1f} lbs.')
    print(f'The angle of the force is {angle:.1f} degrees.\n')


elif option == 3:
    num_forces = int(input('\nHow many forces do you want to add? '))
    forces = []
    angles = []
    number = []
    fx = 0  # Running total of x-component forces
    fy = 0  # Running total of y-component forces
    for i in range(num_forces):
        new_force = float(input(f'\nWhat is the magnitude of force #{i+1} (in lbs)? '))
        new_angle = float(input(f'What is the angle of force #{i+1} (in degrees)? '))
        new_num = i+1
        number.append(new_num)
        forces.append(new_force)
        angles.append(new_angle)
        fx = fx + new_force * math.cos(math.radians(new_angle))
        fy = fy + new_force * math.sin(math.radians(new_angle))

    force = math.sqrt(fx**2 + fy**2)

    if fx > 0 and fy > 0:
            angle = math.degrees(math.atan(fy/fx))
    elif fx < 0 and fy >0:
            angle = math.degrees(math.atan(fy/fx)) + 180
    elif fx < 0 and fy < 0:
            angle = math.degrees(math.atan(fy/fx)) + 180
    elif fx > 0 and fy < 0:
            angle = math.degrees(math.atan(fy/fx)) + 360
    elif fx == 0 and fy > 0:
            angle = 90
    elif fx == 0 and fy < 0:
            angle = 270
    elif fx > 0 and fy == 0:
            angle = 0
    else:
            angle = 180

    print('\nNumber           Force (lbs)          Angle (deg)')
    for i in range(len(forces)):
        print(f'  {number[i]} {forces[i]:>20} {angles[i]:>20}')

    print(f'\nThe magnitude of the resultant force is {force:.1f} lbs.')
    print(f'The angle of the resultant force is {angle:.1f} degrees.')
    print()

else:
    print()
    print('You did not enter a valid option.')
    print()
