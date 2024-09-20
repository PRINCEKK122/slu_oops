guests = []
name = input('Enter a name (blank to end): ')
while name:
    guests.append(name)
    name = input('Enter a name (blank to end): ')
print('You entered', len(guests), 'guests.')