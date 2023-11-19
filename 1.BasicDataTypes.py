Basic data types:
#----------------------------------
# strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). This avoids unnecessary bugs. Some other immutable objects are integer, float, tuple, and bool.
#---------------------------------------
>>set 
myset = {"apple", "banana", "cherry"}
#----------------------------------------------------------------------
>>list
lst=[11,18,9,12,22,23,4,17]
>>> for idx in range(len(lst)):
...     val=lst[idx]
...     if val>15:
...             lost.append(val)
...             lst[idx]=15

>>> for idx,val in enumerate(lst):
...     print(idx,":",val)


#----------------------------------------------------------------------
>> dict

d={1:'sunil', 2:'Yadav', 3:'Kumar'}

#----------------------------------------------------------------------
>>tuple
t=(1,3,5,6)


#----------------------------------------------------------------------
>> list comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#----------------------------------------------------------------------
>>lambda
x = lambda a, b : a * b
print(x(5, 6))

#or 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


#----------------------------------------------------------------------
>>import sys
import sys
 
# total arguments
n = len(sys.argv)
# exiting using 
 sys.exit("Message")  
 
#---------------------------------------------------------------------- 
>> import os
     
# Get the current working directory (CWD)
cwd = os.getcwd()
# Changing the CWD
os.chdir('../')

# Directory
directory = "GeeksforGeeks"
 
# Parent Directory path
parent_dir = "D:/Pycharm projects/"
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory 'GeeksForGeeks' in  '/home / User / Documents'
os.mkdir(path)

#----------------------------------------------------------------------
>> exception in python
# Program to handle multiple errors with one except statement
 
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
 
    # throws NameError if a >= 4
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
 
# note that braces () are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
    
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
#--------------------------------------------------------
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not