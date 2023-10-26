x=50 #global scope variable

def func(x):
    print('x is ',x)
    x=2 #local scope variable
    print('now x is local and value is ', x)

func(x)
print('x is still', x)
