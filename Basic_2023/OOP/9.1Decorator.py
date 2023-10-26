from time import time


def perfomance(func):
    """ Decorator function to print time took to execute function
    """
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f"Time took {t2-t1}s")
    return wrapper

@perfomance
def loop():
    for i in range(100000000):
        i*2

loop()