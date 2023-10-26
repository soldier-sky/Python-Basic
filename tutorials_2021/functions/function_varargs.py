#program to understand how to use variable argument in function. 

def total(a=5, *numbers, **phonebook):
    #here * is used to denote variable argument
    #in this function *number is  tuple  or 1d array and **phonebook contain 2D array or dictionaly
    print('Vale of a ',a)

    #iterate throgh all the itenms in tubple
    for single_item in numbers:
        print('single_item', single_item)

    #iternate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


#calling toatal with var args

total(10,1,2,3,Jack=1123, John=2231, Inge=1560)


