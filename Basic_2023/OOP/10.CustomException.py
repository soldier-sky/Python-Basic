""" Simple program to understand custom/user defined exception in Python
Note: Unlink CPP, in python there it is not mandatory to implemet equivalent of what() method. 
"""
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException as err:
    print(f"Exception occurred: Invalid Age. {err}")


#------------------------------------------------------------
"""To achieve CPP type message from custom execption object, use __init__ method as show below"""
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

try:
    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)
except SalaryNotInRangeError as err:
    print(f"Ooops {err}")