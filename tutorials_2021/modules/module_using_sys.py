import sys
import os

#print('Total commandline arguments are:',sys.argc)  #argc similar to c is not available

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\n The PYTHONPATH is', sys.path, '\n')

print('current working directory is ', os.getcwd())
