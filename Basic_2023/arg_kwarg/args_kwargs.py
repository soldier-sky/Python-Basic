"""
This program is to understand *args and **kwargs (keyword args) in python
"""


def some_function(*args):
    # Simple example to understnad args
    #print(args)         # prints tuple of arguments i.e. (1, 2, 3, 4, 5)
    #print(*args)        # 1 2 3 4 5
    return sum(args)     # python lib sub take varadic argument



def some_function2(*args, **kwargs):
    """ This function demonstrate how to use args and kwargs
    """
    #print(args)         # prints tuple of arguments
    #print(*args)
    #print(kwargs)        # prints dictionary {'num1': 5, 'num2': 10}
    total = 0;
    for items in kwargs.values():
        total += items
    return sum(args) + total
    
    
print("output of summation ", some_function(1,2,3,4,5))
print("output of some_function2 is ", some_function2(1,2,3,4,5, num1=5, num2=10))

# Below function helps to print what these function do
print(help(some_function2))        # This function demonstrate how to use args and kwargs
print(some_function2.__doc__)      #This function demonstrate how to use args and kwargs

print(help(some_function))         # # comment does not work in doc