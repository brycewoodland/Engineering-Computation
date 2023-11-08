# Modify a String
# my_string.upper()
# my_string.lower()
# my_string.capatalize()
# my_string.title()
# my_string.count('a')

#Format a String
# output = 'Hello' + first_name + '' + last_name   creates a single string variable named output
# f'Hello, {first_name}{last_name}'  creates a single formatted string variable named output

# Print a string
# print(output) prints a variable named output
# print (f'Hello,{first_name}{last_name}') prints a formatted string directly (without first assigning it to a variable named output)

"""
Input/Output
Print text and formatted numbers inside of a formatted string
Print(f'The sum is {sum}') displays sum to the default number of decimal places
Print( f 'The sum is {sum:.2f}')    displays sum to 2 decimal places in fixed-point notation
Print( f 'The sum is {sum:.3e}')    displays sum to 3 decimal places in exponent notation
"""

"""
VS Code
Enter by typing py in the terminal window (or python3 in a Mac)
>>> prompt indicates you are in interactive mode
Allows you to execute Python commands directly
Exit by typing quit() or exit()
All work is lost after exiting
"""

"""
Numbers and Calculations
Addition: 4 + 5 (produces 9)
Subtraction: 8 - 2 (produces 6)
Multiplication: 2 * 4 (produces 8)
Division: 15 / 2 (produces 7.5)
Floor division: 15 // 2 (produces 7 since it drops the remainder)
Remainder or modulus: 15 % 2 (produces 1, which is the remainder)
Exponentiation: 2 ** 3 (produces 8)
"""

"""
Libraries
import math (example of using a function: math.sqrt(7))
from math import sqrt (example of using the function: sqrt(7))
from math import * (imports all functions in the math library)
Exploring library functions

Enter interactive mode (type py in the terminal window)
import math [import the math library]
dir(math)  [displays a list or directory of all functions in the math library]
help(math)  [shows some information about each of the functions in the math library]
"""
"""
Structure of IF statements

Basic IF statement
if price >= 1.00:
    tax = 0.07
IF - ELSE structure
if price >= 1.00:
    tax = 0.07
else:
    tax = 0.0
IF - ELIF - ELSE structure
if price >= 1.00:
    tax = 0.07
elif price >= 0.50:
    tax = 0.04
else:
    tax = 0.0
Comparison operators

Greater than:  >
Less than:  <
Greater than or equal to:  >=
Less than or equal to:  <=
Is equal to:  ==
Is not equal to:  !=
Can also use in() operator
if person in('Bob', 'Julie', 'Sam'):
Logical operators

and
if x >= 5 and x <= 10:
or
if x >= 5 or x <= 10:
not
if not x <= 5:
"""
"""
Boolean data

True / False data
my_variable = True  [set up a Boolean variable / Boolean flag]
"""
"""
Trig Functions

Available in the math library
Default unit for angles is radians
math.sin(angle_in_radians)    finds the sine of the angle
math.asin(value)    finds the angle, in radians, whose sine is value
math.degrees(angle_in_radians)    converts an angle from radians to degrees
math.radians(angle_in_degrees)    converts an angle from degrees to radians
"""
"""
Collections

Lists

Lists are collections of items
Create a list with square brackets
friends = ['John', 'Mary', 'Bill']
Access items in a list using an index
print(friends[1])
List methods
friends.append('Sally')    to append an item to the end of the list
friends.insert(0, 'Fred')   to insert an item before index 0
friends.pop(1)                  to "pop" or remove the item with index 1
friends.sort()                    to sort the list in ascending order
len(friends)    to find the length (number of items in) the friends list
Arrays are preferred to lists for doing calculations on groups of numbers
Tuples

Tuples are collections of items
Create a tuple with parentheses
a = (1, 2, 3)
Tuples are immutable (they don't change)
Arrays

Arrays are collections of numbers
We can use the NumPy library to create arrays
"""
"""
Functions & Methods

Useful Functions

Len(variable)     returns the length (number of items in) the specified variable
Methods

Methods are functions that apply to a specific type of object
To call a method use variable_name.method(input_arguments)
Methods always include parentheses (whether or not there are any input arguments)
In interactive mode, type dir(variable_name) to see a list of available methods for that variable type
Methods for string objects
.upper()
.lower()
.title()
.capitalize()
Methods for list objects
.append()
.insert()
.pop()
.sort()
Methods for NumPy array objects
.sum()
.mean()
.std()
.max()
.min()
"""
"""
Libraries

NumPy library

Need to first install the NumPy library using the pip tool
For Windows: py -m pip install numpy --user
For Mac: python3 -m pip install numpy --user
Use the full path to the Python executable if these options don't work
Import numpy as np
Create and operate on arrays using numpy
x = np.array( [ 0, 1, 2, 3, 4, 5 ] )       to create an array of numbers
y = 2 * x                                             to operate on an array element-by-element
print(x[2])                                          to print the item in the x array that has an index value of 2
Many methods for numpy arrays (see Functions & Methods category)
"""
"""
Loops

Structure of a for loop

for variable_name in sequence:
     block of code
friends = ['Bob', 'Julie', 'Sam']
for friend in friends:
     print(friend)
for value in range(5)
     print(value)     prints values from 0 up to, but not including, 5
names = ['Jim', 'Bob', 'Sally', 'Jill']
for i in range(len(names)):
      print(names[i])
      print(names[i], end = ' ')    prints names on the same line
Building a list with a for loop

num_items = 3
items = [ ]
for i in range(num_items):
     new_item = input( f ' What is item # { i + 1 } ? ' )
     items.append(new_item)
     """
"""
Input / Output

Format string values in a formatted print statement

print( f ' {item:<10} ' )     #Left justifies the item variable and uses 10 total spaces
print( f ' {item:>15} ' )     # Right justifies the item variable and uses 15 total spaces
print( f ' {item:^20} ' )     # Center justifies the item variable and uses 20 total spaces
"""

"""
Loops

Structure of a while loop

while condition:
     block of code
x = 0
while x <= 5:
     print(x)
     x = x + 1     or x += 1
Ctrl-c to get out of an infinite loop
Building a list with a while loop

items = [ ]
item = 'initial value'
while item != 'End':
     item = input( f " Enter new item ('end' to quit): " ).capitalize( )
     if item != 'End':
          items.append(item)
          """

"""
Functions

Define a function

def square_number(number):
     number_squared = number ** 2
     return number_squared
Note: input parameters and return commands are not required elements of a function
Call a function

function_name()       for function with no input parameter or return value
function_name(input_argument)       for function with an input parameter
function_name(arg1, arg2)      for function with multiple input parameters
result = function_name(input_arg)     for function with input parameter and return value
"""

'''
Scatter Plots

Create a scatter plot

import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()
Create a series of sequential numbers

Use a list
Use the NumPy arange() function
np.arange(start_value, stop_value, increment)
Does not include the stop value
Use the NumPy linspace() function
np.linspace(start_value, stop_value, num_points)
Includes the stop value
Customize a plot

plt.plot(x,y, option =  …)
marker =
'.' (point)
',' (pixel)
'o' (circle)
'v' (triangle_down)
'^' (triangle_up)
'*' (star)
's' (square)
'd' (diamond)
Etc.
linestyle =
'-' (solid)
':' (dotted)
'- -' (dashed)
'-.' (dashdot)
color =
'b' (blue)
'g' (green)
'r' (red)
'c' (cyan)
'm' (magenta)
'y' (yellow)
'k' (black)
'w' (white)
Etc.
linewidth = 2
markersize = 12
Symbols can be passed in together in a "shortcut string"
plt.plot(x,y,'o-k')
Add or customize chart elements

plt.title('my_title', size = 12, weight = 'bold')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.grid(True)
plt.xlim(0,5)
plt.ylim(0,10)
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6])
Plot multiple series on the same graph
plt.plot(x1,y1,label = 'Series 1')
plt.plot(x2,y2,label = 'Series 2')
plt.legend(loc = 'upper left')
plt.show()
'''
'''
Functions & Methods

Functions in the NumPy library

roots function (finds roots of a polynomial)
coef = list (or array) of polynomial coefficients
roots = np.roots(coef)
Input / Output

Print text + formatted numbers

print( f 'The sum is {sum:10.2f}' )  [displays sum using at least 10 total spaces, with 2 digits after the decimal]
'''
'''
Functions & Methods

Functions for linear algebra

Functions in the NumPy library (np)
array function to define 1D vector
np.array([1, 2, 4])
Input is a list
array function to define a 2D matrix
np.array( [ [2,3,5], [1,2,6], [3,4,9] ] )
Input is a list of lists
Each list is a row in the matrix
dot function to multiply two matrices
np.dot(matrix_1, matrix_2)
Functions in the linalg module of NumPy
det function to find the matrix determinant
np.linalg.det(matrix)
inv function to find the matrix inverse
np.linalg.inv(matrix)
solve function to solve a system of linear equations
np.linalg.solve(A_matrix, b_vector)
zeros function to create an array of  zeros
a = np.zeros(5)    creates a 1D array of 5 zeros
ones function to create an array of ones
b = np.ones((2,3))    creates a 2D array of ones, with 2 rows and 3 columns
Assign and retrieve values in an array using an index

print(a[2])          prints the value in the 1D a array that has an index of 2

print(b[1,2])       prints the value in the  2D b array that has an index of 1 for the row and 2 for the column

a[2] = 10           assigns the value 10 to the location in the 1D a array that has an index of 2

b[1,2] = 25        assigns the value 25 to the location in the 2D b array that has an index of 1 for the row and 2 for the column

Loops

Nested for loops to create a 2D array (3 by 3 in this example)

A = np.zeros((3,3))           initialize the A matrix with all zeros

for row in range(3):

     print(f ' Values for row {row + 1} ' )

     for column in range(3):

          A[row, column] = float(input(f ' Column {column+1}: ' )
          '''
'''Collections

Indexing into a list or array

x[2] accesses the item in the x array that has an index of 2
x[-1] accesses the last item in the x array
Indexing starts with 0'''