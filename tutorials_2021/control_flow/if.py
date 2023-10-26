#example program to understand if control statement

number=30
guess=int(input('Please enter and integer: '))

if guess == number:
    #new block starts here
    print('Congratulations!!! you\' guessed it right')
    print('{but you do not win any prizes}')
    #new block ends here
elif guess < number:
    print('No, it is little higher that that')
else:
    print('No,it s a little lower thatn that')

print('Done')




