# Demo basic while loop structure
# x = 0
# while x <= 10:
#     print(x)
#     x= x + 1

# num = 0
# count = 0
# sum = 0
# print()
# while num < 10:
#     num = int(input('Please enter an integer: '))
#     if num < 10:
#         count += 1 
#         sum += num

# print(f'\nYou entered {count} integers that were less than 10')
# print(f'The sum of those {count} integers was {sum}\n')

friends = []
add_friend = 'initialize'
print()

while add_friend != 'End':
    add_friend = input("Enter a friend's name (or 'end' to quit): ").capitalize()
    if add_friend != 'End':
        friends.append(add_friend)

print(f'\nYou have {len(friends)} friends in your list.')
print(f'Your friends are {friends}\n')
