integer =int(input('Add the integers from 1 up to and including what integer? '))
sum = 0
for i in range(integer):
    sum = sum + (i+1)
print(f'\nThe sum of all integers from 1 up to and including {integer} is {sum}.\n')
