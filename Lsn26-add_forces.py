import math

num_forces = int(input('\nHow many forces do you want to add? '))
forces = []
angles = []
fx = 0  # Running total of x-component forces
fy = 0  # Running total of y-component forces
for i in range(num_forces):
    new_force = float(input(f'\nWhat is the magnitude of force #{i+1} (in lbs)? '))
    new_angle = float(input(f'What is the angle of force #{i+1} (in degrees)? '))
    forces.append(new_force)
    angles.append(new_angle)
    fx = fx + new_force * math.cos(math.radians(new_angle))
    fy = fy + new_force * math.sin(math.radians(new_angle))

force = math.sqrt(fx**2 + fy**2)

print(f'\nThe magnitude of the resultant force is {force:.2f} lbs.\n')
