#example program for break statement 

while True:
    s=input('Enter somthing in text: ')
    if s == 'quit':
        break
    print('lenght of input string is ', len(s))


print('Done')
