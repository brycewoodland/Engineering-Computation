import math
integer = int(input('What integer do you want to find the factorial of? '))
print()
print('Using a for loop:')
product = 1
for i in range(1,integer+1):
    product = product * i
print(f'The factorial of {integer} is {product}.')
print()
print('Using the built-in function from the math library: ')
print(f'The factorial of {integer} is {math.factorial(integer)}.')
print()