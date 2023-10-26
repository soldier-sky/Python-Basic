# Understanding special dunder methods

class MyVector:
    def __init__(self, in_list):
        self.in_list = in_list
        self.lenght = len(in_list)
    
    def __str__(self):
        return "My custom Vector"
    
    def __getitem__ (self, idx):
        """ Overloading [] operator"""
        return self.in_list[idx]


temp = [1,2,3,4,5,6,7,8,9]

my_vector = MyVector(temp)
print(str(my_vector))
print(my_vector[3])