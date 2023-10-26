#program to understand continue statement in python

while True:
    s = input("Enter something: ")
    
    if s== 'quit':
        break
    if len(s) < 3:
        print ('Too small')
        continue
    print('Input is out of sufficient length')


