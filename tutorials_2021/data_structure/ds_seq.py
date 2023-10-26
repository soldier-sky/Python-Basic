#this program is to learn how sequencing work and how to use slicing on ds.

shoplist=['apple', 'mango', 'carrot', 'banana'] #list of fruit
name='Sunil Yadav'

#indexing or subscription operation#

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])

print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
#print('Item 4 is', shoplist[4])
print('Item -1 is', shoplist[-1])


print('Item -2 is', shoplist[-2])
print('Charater 0 is', name[0])

#Slicing on a list#
print('Item 1 to 3 is', shoplist[1:3])

print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1]) #similar to 1:3

print('Item start to end is',shoplist[:])

#slicing on a string#
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is',name[:])


