# Python program to
# demonstrate private members
 
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "BaseClassA"
        self.__c = "BaseClassC"                     #private member
        self._p=10									#protected member p
    def print_private(self):
        print(f"value of private c: {self.__c}")

# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        self.print_private()   
        print(f"value stored in protected p is {self._p}")
# Driver code
obj1 = Base()
obj1.print_private()
#print(obj1.__c)                # private object can't be access.
print(obj1._p)                # protected object can be accessed.
obj2 = Derived()
