"""
This example program is to get familiar with file IO
"""
filename = 'log.txt'
fin = open(filename, 'r')    # open file in read mode. ensure you cd to directory containing log.txt file
                             # refer https://docs.python.org/3/library/pathlib.html for more options on how to handle paths

print(fin.read())            # reads complete file in one time
fin.seek(0)                  # set read cursor to start of file
print(fin.readline())        # reads single lines at a time
print(fin.readline())
print(fin.readline())

print(fin.readlines())       # reads multiple lines at a time in list

fin.close()                  # close the file post read operation

# To avoid explicit call to file close(), we can use below approch

with open(filename, 'r') as f:
    print(f.readlines())

with open('out.txt', 'w') as fout:
    txt = fout.write("this is sample write operation")
    print(f'Wrote {txt} characters into the file')
