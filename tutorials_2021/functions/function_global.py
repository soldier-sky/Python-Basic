#sample program to understand how to access global varible in function


x=50

def func():
    global x
    print('x is ',x)

    x=2
    print('changed global valu of x is ',x)

func()
print('value of x is',x)
