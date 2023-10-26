print('simple assignment')

shoplist=['apple', 'mango', 'carrot', 'banana']
#mylist is just another name pointing to same list
mylist=shoplist

#I purchased the first item, so I removed it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is' , mylist)
#Above two print statement will have same output without 'apple'

print('copy by making a full slice')

mylist=shoplist[:]

#remove first item
del mylist[0]
mylist.remove('banana')
print('shoplist is', shoplist)
print('mylist is' ,mylist)
