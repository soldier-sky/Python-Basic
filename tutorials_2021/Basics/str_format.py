#this program is to get familiar with format() used to alter string

age =29
name= "Sunil Kumar Yadav"

print ('{0} was {1} years old when he wrote this program'.format(name, age))
print('Why is {0} playing with that python'.format(name))

print("printing message again")
#printing same messge by removing numbers and passing parmameter name
print ('{} was {} years old when he wrote this program'.format(name, age))
print('Why is {name} playing with that python'.format(name=name))


#python 3.6 way of using format: useing f string

print(f'{name} was {age} years ld when he wrote this program')


