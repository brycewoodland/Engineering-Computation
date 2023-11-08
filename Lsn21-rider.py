"""
File: rider.py
Author: Bryce Woodland
Date: 11/1/2022
Purpose: Determine if a person may ride a ride 
at an amusement park
"""

# Get input from the user
print()
height = float(input('What is your height in inches?'))
age = int(input('What is your age?'))
riders = input('How many riders (single/multiple)?')

# Determine if the person can ride
if height >=36 and (age >= 18 or riders.lower() == 'multiple'):
    can_ride = True
else:
    can_ride = False

# Display whether or not the person can ride
if can_ride:
    print('You can ride this ride. Have fun!')
else: 
    print("You cannot ride this ride. We're sorry.")
print()

