#sample program to understand default parameter of function

def say(message='no input value', times=1):
    #default value like say(message='str', times) wont work
    print(message*times)

say('Hello')
say('Hello',3)

say() #will use default value for message and times/
