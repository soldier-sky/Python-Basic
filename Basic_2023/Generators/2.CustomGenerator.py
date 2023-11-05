"""
Example programm to understand how to create own iterator,
with next functionality similar to inbuilt types like List etc.
"""


class MyGenerator:
    """ Example generator 
    """
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # Overload iter()
    def __iter__(self):
        return self
    
    # Overload next()
    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration


g = MyGenerator(0,100)
for i in g:
    print(i)
