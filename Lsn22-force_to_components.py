# Given a force and an agle, find the
# x and y components of the force

import math
print()

# Get input from the user
force = float(input('What is the magnitude of the force (in lbs)?'))
angle = float(input('What is the angle of the force (in degrees)?'))

# Calculate x and y component forces
fx = force * math.cos(math.radians(angle))
fy = force * math.sin(math.radians(angle))

# Display results
print()
print(f'The x-component of the force is {fx:.1f} lbs.')
print(f'The y-component of the force is {fy:.1f} lbs.')
print()

