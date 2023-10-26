# tuple declaration do not require parathesese but we should use it
# to indicate start and end of tuple
# explicit is better than implicit

zoo=('python', 'elephant', 'penguin')  #tuble of zoo animal

print('Number of animals in the zoo is ', len(zoo))

new_zoo= 'monkey', 'camel', zoo #paramntheses not required but good to use them
print('Number of cases in ther new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Anials brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animalz in the new zoo is', len(new_zoo)-1+len(new_zoo[2])) 

