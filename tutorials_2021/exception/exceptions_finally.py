
import sys
import time

f =None

try:
    f= open("poem.txt")
    # Our usal file- reading idom
    while True:
        line = f.readline()
        if len(line) == 0:
            break

        print(line, end=' ')   # As read line have \n 
        sys.stdout.flush()
        print("Press ctrl+c now")
        # To make sure it runs for a while
        time.sleep(2)

except IOError:
    print('Could not find file poem.txt')

except KeyboardInterrupt:
    print('!! you cancelled the reading from the file.')


# Finally block to close or cleanup operation if exception is raised
finally:
    if f:
        f.close() # close file if exception occure before file io operation
    print("(Cleaning up : Closed the file)")


