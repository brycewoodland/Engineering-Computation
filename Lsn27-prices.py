# Create and display lists of items and prices

# Display message to the user
print('\nEnter items and their corresponding prices')

# Initialize lists and variables
items = []
prices = []
item = 'initial value'

# Build lists
while item != 'End':
    item = input(f"\nWhat item do you want to add ('end' to quit)? ").capitalize()
    if item != 'End':
        price = float(input(f'What is the price of {item.lower()}? $'))
        items.append(item)
        prices.append(price)

# Print results - first show just print(items) and print(prices)
print('\nItem       Price')
for i in range(len(items)):
    print(f'{items[i]:<10} ${prices[i]:.2f}')

# Calculate summary statistics
max_price = prices[0]
max_item = items[0]

for i in range(len(items)):
    if prices[i] > max_price:
        max_price = prices[i]
        max_item = items[i]

print(f'\nThe total price of all the items is ${sum(prices):.2f}')
print(f'{max_item} had the highest price of ${max_price}\n')