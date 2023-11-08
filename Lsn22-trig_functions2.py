import math

print()

# Scenario 1
A = 25  # Degrees
a = 3   # inches
b = a/math.tan(math.radians(A))
c = math.sqrt(a**2+b**2)
B = math.degrees(math.atan(b/a))
print(f'For scenario 1, the length b is {b:.3f} inches.')
print(f'For scenario 1, the length c is {c:.3f} inches.')
print(f'For scenario 1, the length B is {B:.3f} degrees.')
print()
# Scenario 2
a = 2   # inches
c = 4   # inches
b = math.sqrt(c**2-a**2)
A = math.degrees(math.atan(a/b))
B = math.degrees(math.atan(b/a))
print(f'For scenario 2, the length b is {b:.3f} inches.')
print(f'For scenario 2, the angle A is {A:.3f} degrees.')
print(f'For scenario 2, the angle B is {B:.3f} degrees.')
print()
# Scenario 3
b = 1   # inches
c = 3   # inches
a = math.sqrt(c**2-b**2)
A = math.degrees(math.atan(a/b))
B = math.degrees(math.asin(b/c))
print(f'For scenario 3, the length a is {a:.3f} inches.')
print(f'For scenario 3, the angle A is {A:.3f} degrees.')
print(f'For scenario 3, the angle B is {B:.3f} degrees.')
