#friends = ['Jim','Julie']
friends = []
friends.append('Jim')
friends.append('Julie')
friends.insert(1,10)
friends.append('Fred')
friends.pop(1)
friends.sort()

print(friends)
print(friends[0])
print(friends[1])
print(f'There are {len(friends)} items in the friends list')

