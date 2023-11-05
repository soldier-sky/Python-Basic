"""
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
The yield keyword is used to produce a value from the generator and pause the generator function's execution until the next value is requested.
Syntax of generator functions looks like this:

def generator_name(arg):
    # statements
    yield something

Note: Generators take less space in memory as it returns one value/object at a time from iterable
Hence its being used in standard libraries
"""

def my_generator(num):
    for i in range(num):
        yield i

g = my_generator(10);
next(g)  # my_generator() returns 0
next(g)  # my_generator() returns 1

print(next(g))    # prints 2
#StopIteration will be thrown once reached the end of iterator