class Person:
    def __init__(self,name):
        #__init__ method is equivalent to constructor in CPP
        self.name=name
    def say_hi(self):
        print('Hello, my name is ',self.name)

        
p_obj=Person("Sunil Kumar Yadav")
p_obj.say_hi()

#above statement could be written as Person("Sunil").say_hi()

