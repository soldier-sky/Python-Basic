# from cmd line use below command without improt of pdb and pdb.set_trace()
# python -m pdb pdb_example.py
# Note: use 'bt' for stack trace. use 'args' or 'a' to print all the arguments of function which is currently active
# setting breakpoint: break filename: lineno, condition, Use break to list all BP
# After adding breakpoints with the help of numbers assigned to them we can manage the breakpoints using the enable and disable and remove command. e.g. disable 1
#



#import pdb
  
  
def addition(a, b):
    answer = a + b
    return answer
  
  
#pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)