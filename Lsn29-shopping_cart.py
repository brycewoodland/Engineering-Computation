"""
File: shopping_cart.py
Author: Bryce Woodland
Date: 11/20/2022
Purpose: Use a while loop to help create a shopping cart list
"""

option = ''
items = []
prices = []
while option != '4':
    if option != '4':
        print('\nWelcome to the Shopping Cart Program!\n')
        print('Please select one of the following:')
        print('1. Add item')
        print('2. List items & total price')
        print('3. Remove item')
        print('4. Quit')
        option = input('Which option do you want? ')
        if option == '1':
            item = input('\nWhat item would you like to add? ')
            price = float(input(f'What is the price of {item}? $'))
            items.append(item.capitalize())
            prices.append(price)
            print(f'{item.capitalize()} has been added to your cart.\n')
        elif option == '2':
            print('\nThe contents of the shopping cart are:')
            for i in range (len(items)):
                print(f'{i+1}. {items[i]:<10} ${prices[i]:<10}')
            print(f'\nThe total price of all the items is ${sum(prices):.2f}')
        elif option == '3':
            old_item = int(input('\nWhat item would you like to remove? '))
            if old_item > len(items):
                print(f'You do not have {old_item} items in your cart.')
                print('Please select another option.')
            else:
                old_item = old_item-1
                print(f'{items[old_item]} has been removed from your cart.')
                items.pop(old_item)
                prices.pop(old_item)
        elif option == '4': 
            print('\nThank you for shopping with us. Goodbye.\n')
        else:
            print('\nThat is an invalid entry. Please select again.')
