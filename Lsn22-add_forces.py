import math
print()
print('This program will addd two forces together and display the resultant force and angle.')
print()

# Get input from the user
first_magnitude = float(input('What is the magnitude of the first force (in lbs)?'))
first_angle = float(input('What is the angle of the first force (in degrees)?'))
second_magnitude = float(input('What is the magnitude of the second force (in lbs)?'))
second_angle = float(input('What is the angle of the second force (in degrees)?'))
print()

# Calculate the x and y components
fx1 = first_magnitude*math.cos(math.radians(first_angle))
fy1 = first_magnitude*math.sin(math.radians(first_angle))
fx2 = second_magnitude*math.cos(math.radians(second_angle))
fy2 = second_magnitude*math.sin(math.radians(second_angle))
fx = fx1 + fx2
fy = fy1 + fy2
force = math.sqrt(fx**2+fy**2)
print()

# if loop
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

# Display the results
print(f'The magnitude of the resultant force is {force:.1f} lbs.')
print(f'The angle of the resultant force is {angle:.1f} degrees.')

