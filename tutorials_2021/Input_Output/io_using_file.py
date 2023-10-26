poem='''\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use python
'''

# writing into a file
f=open('poem.txt','w')
f.write(poem)
f.close()

# Read operation
f=open('poem.txt') # Default mode is read
while True:
    line = f.readline()

    if len(line) == 0:
        break

    print(line, end=' ')  # Since content from file already have newline i.e. \n, we are using end =' '

f.close()
