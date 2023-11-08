# Function that performs a task
# def print_message():
#     print('\nYou just called the print_message function!\n')

# print_message()

# Function that recieves an input value and
# performs a task on that input value
# def square_number(number):
#     number_squared = number**2
#     print(f'The value of {number} squared is {number_squared}\n')

# square_number(3)

# Function that recieves an input value and, peforms a task
# on that input value, and returns an output value
def square_number(number):
    number_squared = number**2
    return number_squared

# result = square_number(3)
# print(result)
print(f'\nThe result is {square_number(3)}.\n')