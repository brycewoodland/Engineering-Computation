# Work with a list of friends
friends = ['Bob','Sally','Jill']
print(f'Your current friends are {friends}.')

print('\nWhat would you like to do? ')
print('Option 1: Add a friend')
print('Option 2: Remove a friend')
print('Option 3: Sort your friends')
print('Option 4: Count your friends')
print('Option 5: Quit')

select = int(input('\nEnter your selection: '))

if select == 1:
    new_friend = input('Who is the friend you would like to add? ')
    friends.append(new_friend)
    print(f'Your new list of friends is {friends}. ')
elif select == 2:
    old_friend = int(input('What is the number of friend you want to remove? '))
    friends.pop(old_friend - 1)
    print(f'Your new list of friends is {friends}. ')
elif select == 3:
    friends.sort()
    print(f'Your sorted list of friends is {friends}. ')
elif select == 4: 
    print(f'You have {len(friends)} friends. ')
else:
    print('Have a nice day!')
    print()

