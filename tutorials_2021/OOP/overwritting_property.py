# over riding @property in derived class

class Base:
    def __init__(self,x,y):
        self._x=x;
        self._y=y;
        print("Inside Base Init")
        
    #Getter for x
    @property
    def x(self):
        return self._x;
        
    @x.setter
    def x(self, val):
        self._x=val


class Derived(Base):
    def __init__(self, x, y):
        Base.__init__(self,x,y)
        print("Inside Derived Init")
        
    @Base.x.getter                  #overriding getter from Base class
    def x(self):
        print("Inside Derived getter")
        return self._x
        
    @Base.x.setter
    def x(self,val):
        print("Inside Derived Setter")
        self._x=val

b= Base(10,20)
b.x+=100

print(b.x)
print("========================")

d=Derived(11,22)
d.x+=5
print(d.x)
