try:
    text = input('Enter something ---->')
except EOFError:
    print('wWhy did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')

else:
    print ('You entered {}'.format(text))

