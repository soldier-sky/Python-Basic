"""
Simple example to understand what are decorators and how to use them in python. Decorators super chargs function.
Something similar to Higher order function.
@ -> denotes decorator start
"""

# Higher order function
def greet(func):
    func()

def new_greed():
    def func():
        return 5
    return func

def print_msg():
    print("sample message!")

print(greet(print_msg))

#--------------------------------------------------------------------------
# Decorator definition i.e. function which will be called.
# Under the hood decoratrs called similar to higher order function
def my_decorator(func):
    """
    decorator function will call the function on which its being applied and 
    additional routines mentioned in wrapper function will execute.
    """
    def wrapper_function():
        print("----- Start of decorator ---------")
        func()
        print("----- End of decorator ---------")
    return wrapper_function


@my_decorator
def greeting():
    print("Hello")

greeting()
# Note if greeting() funtion is chagned to greeting(msg) then we need to update our decorator function. 
# To avoid this we can use updated decorator definition.

def my_new_decorator(func):
    def wrapper_function(*args, **kwargs):
        print("----- Start of decorator ---------")
        func(*args, **kwargs)
        print("----- End of decorator ---------")
    return wrapper_function

@my_new_decorator
def custom_greeting(name):
    print("Hello ", name)

@my_decorator
def greeting2():
    print("Hello 2")

custom_greeting('Sunil')
greeting2()