def print_max(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integerts.'''
    #convert to integers, if possible

    x=int(x)
    y=int(y)

    if x>y:
        print(x,' is maximum')
    else:
        print(y, ' is maximum')

print_max(5,7)
print(print_max.__doc__)
