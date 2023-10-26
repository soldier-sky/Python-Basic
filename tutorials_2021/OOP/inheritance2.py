
class SchoolMember:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Inside SchoolMember Constructor\n")

    def tell(self):
        print("My name is  {} and my age is {}".format(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("inside Teacher constrctor\n")

    def tell(self):
        SchoolMember.tell(self)
        print("My salary is {}".format(self.salary))


Tobj=Teacher("Sunil Kumar Yadav", 29, 100000)
Tobj.tell()


 
