# Convert pressure in lbs/ft^2 to pressure in lbs/in^2 (or psi)

pound_force_inch = input('Enter the value of PSI: ')
pound_force_foot = input('Enter the value of PSF: ')
pound_force_inch = float(pound_force_foot)/144
print(f'That value is {pound_force_inch} PSI.\n')
