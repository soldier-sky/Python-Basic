class Point:
    INSTANCE_COUNT=0        #Class attribute
    def __init__(self, x):
        self._x=x     #protected  #self.* are instance attribute
        self._y=0
        self.__z=0    # __ for private
        self.data=1111
        Point.INSTANCE_COUNT+=1

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x=x

    #getter
    @property
    def x(self):              
        return self._x

    @x.setter
    def x(self, newx):        #getter
        if(newx>1000):
            print("value too high")
        else:
            self._x= newx

    def get_instance_count(self):
        return Point.INSTANCE_COUNT

    @staticmethod
    def print_data():
        print(r'dummy:',Point.INSTANCE_COUNT)

    @classmethod
    def get_instance(cls,x):
        return cls(x)



class Point2d(Point):
    def __init__(self, x,y):
        #Point.__init__(self, x)
        super().__init__(x)
        self._y= y
        self._z= 0

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y= y



p1=Point(33)
print(p1.get_x())
print(p1.get_y())

print("Point ref count:",p1.get_instance_count())

p11=Point(3)
print(p11.get_x())
print(p11.get_y())

print("Point ref count:",p1.print_data())

p12=p11.get_instance(12)
print("priting p12.get_x: ",p12.get_x())

print("After aplying class method update",p11.get_x())

p1.x=111       #calling Point setter

print(p1.x)    # calling Point getter

print("-----------------------")
p2=Point2d(44,55)
print(p2.get_x())
print(p2.get_y())