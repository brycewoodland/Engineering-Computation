"""
File:Lsn20-meal_price_calculator.py
Author: Bryce Woodland
Date: 10/29/22
Purpose: Calculate the price of a meal
"""

print('This program will calculate the total price of a meal.')

# Get information from the user
print()
child_meal = float(input("What is the price of a child's meal? (in dollars)? "))
adult_meal = float(input("What is the price of an adult's meal (in dollars)? "))
num_children = int(input('How many children are there? '))
num_adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate (enter 0.05 for 5%)? '))

# Perform Calculations
subtotal = child_meal*num_children + adult_meal*num_adults

# Print Payment Amount
print()
print('Suggested Tip Amounts:')
print(f'     15% = ${subtotal*.15:.2f}')
print(f'     18% = ${subtotal*.18:.2f}')
print(f'     20% = ${subtotal*.20:.2f}')
print()

# More information from user
tip_amount = float(input('Please enter a tip amount (in dollars): '))

# Perform Calculations
subtotal = child_meal*num_children + adult_meal*num_adults
total = subtotal + subtotal*tax_rate + tip_amount

# Print Payment Amount
print()
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${subtotal*tax_rate:.2f}')
print(f'Tip: ${tip_amount}')
print('---------------------------')
print(f'Total: ${total:.2f}')
print()
print()

# Final info from user
payment_amount = float(input('What is the payment amount (in dollars)? '))

# Print final information
print(f'Change: ${payment_amount - total:.2f}')
print()
print('Thank you for dining with us!')
