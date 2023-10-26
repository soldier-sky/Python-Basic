
import pickle

# Name of the file where we will stor the object
shoplistfile= 'shoplist.data'

# List of item
shoplist = ['apple', 'mango', 'carror']

# write to file
f= open(shoplistfile, 'wb')
# Sump the object into file
pickle.dump(shoplist,f)
f.close()

# Destroy the shoplist variable
del shoplist


# Read back from storage
f=open(shoplistfile,'rb')
# load the object from file

storedlist=pickle.load(f)
print(storedlist)
f.close()
