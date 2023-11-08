# Create and display lists of items and prices

# Get input from the user
num_items = int(input('\nHow many items do you need to enter prices for? '))

# Initialize lists
items = []
prices =[]

# Build lists
for i in range(num_items):
    new_item = input(f'\nWhat is item #{i+1}? ').capitalize()
    new_price = float(input(f'What is the price of {new_item.lower()}? $'))
    items.append(new_item)
    prices.append(new_price)

# Print results
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
