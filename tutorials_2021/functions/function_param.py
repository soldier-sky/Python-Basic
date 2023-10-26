#program to understand function parameter in python

def print_max(a,b):
    if a>b:
        print(a, ' is maximum')
    elif a==b:
        print(a, 'is equalto',b)
    else:
        print(b, ' is maximum')

#Call function print_max()

print_max(3,4)

x=6
y=12

print_max(x,y)
