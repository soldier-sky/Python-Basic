def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def is_palindrome_refined(text):
    '''This program ignores whitespaces and punchuations 
    then perform palidrome_test'''
    temp=text.replace(' ','')  #replace white spaces with nothing
    temp=temp.replace(',','')  #replace , with nothing
    return is_palindrome(temp.lower())

something=input("Please enter text: ")

if is_palindrome_refined(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')

