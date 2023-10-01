# conditional statements and  loop control
# Note: Index in python start with 0

value= 88;
while True:
    guess=float(input("Please enter valid integer: "))
    if guess>value:
        print("Guessed value is larger than in built value. Please try again")
    elif guess<value:
        print("Guessed value is smaller than in built value. Please try again")
    else:
        print("Guessed value is correct.")
        break


for x in range(1,100):
    print(x)