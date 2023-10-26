#sample program to learn while loop

number=23
running=True

while running:
    guess =int(input('Please enter an integer'))

    if guess ==number:
        print('congratulations, you guessed it')
        running=False
    elif guess < number:
        print('No, it is little higher than that.')
    else:
        print('No, it is little lower than that')

else:
    print('The` while loop is over.')

print('Done...')

