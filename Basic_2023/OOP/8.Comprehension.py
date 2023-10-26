"""
This example shows how comprehension work with 
few of the standard data types.
"""

# List Comprehension
# Syntax:
# new_list = [param for param in iterable]

my_list = list(range(10))
print("my list: ", my_list)

square_list = [num**2 for num in my_list]
print("squared list: ",square_list)

odd_list = [num for num in my_list if num%2!=0]
print("odd list: ",odd_list)

print("------------------------")
#-----------------------------------------------------------------------------------------------------
# Set Comprehension
# Syntax:
# new_list = {param for param in iterable}

my_set = set(range(10))
print("my set: ", my_set)

square_set = {num**2 for num in my_set}
print("squared set: ",square_set)

odd_set = {num for num in my_set if num%2!=0}
print("odd set: ",odd_set)
print("------------------------")
#-----------------------------------------------------------------------------------------------------
# Dict Comprehension
# Syntax
# new_dict = {key:value(operation) for key,value in dictionary.items() }
my_dict = {
    'a':1,
    'b':2,
    'c':3
}

square_dict = {key:value**2 for key,value in my_dict.items() }
print("my square dict: ", square_dict)
#-----------------------------------------------------------------------------------------------------
# finding duplicate from list using comprehension
example_list = [1,3,4,6,2,3,8,4,10,0,5]      # [3,4] are duplicate
dublicate = [num for num in example_list if example_list.count(num)>1 ]   # returns [3, 4, 3, 4]
solution = list(set(dublicate)) # returns [3, 4]. 
# Note Typecasting can be done directly in above expression but for readiablity seperated 
print(solution)