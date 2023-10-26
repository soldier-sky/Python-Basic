#'ab' is short for 'a'ddress 'b'ook

ab={ 'Swaroop':'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'}

print("Swaroop's address is ", ab['Swaroop'])

#Deleting a key-value pair

del ab['Spammer']

print('\n There ar {} contacts in th address-bookn'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name,address))

#Addding a key-value pair

ab['Guido']='guio@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
