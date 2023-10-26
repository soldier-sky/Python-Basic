#sample program to return maximum of  input values

def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(45,60))
print(maximum(55,55))
print(maximum(55,30))
