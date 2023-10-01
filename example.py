# example program to get familiar with Python classes

class Person:
    def __init__(self, name, age):
        self._name=name
        self._age=age
        
    def print_age(self):
        print("age of person is ",self._age)
        
    def print_name(self):
        print("name of the person is ",self._name)

class Employee(Person):
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self._company=company
        
    def print_details(self):
        Person.print_age(self)
        Person.print_name(self)
        print("company name is ", self._company)
    def print_age(self):               # overriding print_age
        self._age=33
        print("over ridden age of person is ",self._age)

p=Person("Sunil", 30)
p.print_age()
p.print_name()

e=Employee("Sunil", 30, "Vector")
e.print_details()
e.print_age()