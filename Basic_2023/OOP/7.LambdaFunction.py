# Example program to understand Lambda function
my_list = list(range(1,10))
print(my_list)

double_numbers = (lambda num:num*2)
print(double_numbers(my_list))

# new list using Square of each element of my_list
new_list =list(map(lambda num: num**2, my_list))
print(new_list)

tuple_list = [(0,5), (88,60), (9,3)]
#tuple_list.sort() # sort in place using default key. # OP: [(0, 5), (9, 3), (88, 60)]
tuple_list.sort(key=lambda x:x[1])    # sort using second element of tuple in list

print(tuple_list)

lfunc = map(lambda num: num**2, my_list)
#print(lfunc(my_list))
for m in lfunc:
    print(m)

print("--------------------------")

def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y

# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))
