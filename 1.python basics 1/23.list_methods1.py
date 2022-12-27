basket=[1,2,3,4,5]
print(len(basket))

#adding
#append
basket.append(100)
print(basket)
'''
if we do print(basket.append(100)) it will show none 
because append changees initial list but it doesnt have a value so it shows none

'''
#ins
basket.insert(0,50)#it inserts the given object in given index
print(basket)
#extend
basket.extend([110,101])
print(basket)
'''
all the above methods only moodifly the list they dont create a copy
'''

