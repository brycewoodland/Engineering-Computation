# Solve for unknown values of a right triangle

import math
print()

# Scenario 1
A = 75  # degrees
a = 2   # inches
b = a/math.tan(math.radians(A))
print(f'For scenario 1, the length b is {b:.3f} inches.')

# Scenario 2
a = 3   # inches
c = 5   # inches
B =math.degrees(math.acos(a/c))
print(f'For scenario 2, the angle B is {B:.3f} degrees.')

# Scenario 3
a = 1   # inches
c = 4   # inches
A = math.degrees(math.asin(a/c))
print(f'For scenario 3, the angle B is {A:.3f} degrees.')

# Scenario 4
a = 2   # inches
b = 4   # inches
B = math.degrees(math.atan(b/a))
c = math.sqrt(a**2 + b**2)
print(f'For scenario 4, the angle B is {B:.3f} degrees.')
print(f'For scenario 4, the angle c is {c:.3f} inches.')
print()
