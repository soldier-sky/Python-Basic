# This program is to understand how to use inheritance in Python

# Parent or super class
class SchoolMember:
    '''Represent any school memeber.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell me details.'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=' ')

# Child or subclass
class Teacher(SchoolMember):
    '''Represents a  teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary= salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary : "{:d}"'.format(self.salary))


# Child or subclass
class Student(SchoolMember):
    '''Represent a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print('(Iniitialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t= Teacher('Ms. Shrividya', 40, 30000)
s= Student('Sunil Yadav', 29, 75)

#Print a blank line
print()

members = [t, s]

for member in members:
    #works for both Teacher and Stuents
    member.tell()













