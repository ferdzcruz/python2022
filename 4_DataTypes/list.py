from common_vars import *
# '''A list is value that contains multiple values in ordered sequence'''

print(name[0])  #name is the name of the list
                #[0] is the index. This can only be integer
print('===============')
# #concatinate
print(f"{name[0]} is the daddy, {name[1]} is the mommy, {name[2]} is the child")
print('===============')
# #This ignore the index error since value is out of the range
try:
    print(name[4])
except IndexError: print("Not on the list")
print('===============')
try:
    print(name[1.0])
except TypeError: print("cannot be float")
print('===============')
# #List also can contain other values


print(animals[0][1]) #index 0, with bowie as index 1 of index 0
print(animals[1][1])
print(f"{animals[0][0]} is a dog, {animals[1][0]} is a cat")
print('===============')
# #Changing the values
animals[1][0] = 'muffin'
print(animals[1][0])
print('===============')
# #count the number of the list
print(len(name),type(name))
print(len(animals),type(animals))
print('===============')


#contination
 #commor_vars have all the variables
spam = spam + ['A', 'B', 'C']
print(spam)

#using for loops in list
for spam_l in spam:
    print(spam_l)
print('===============')

#using range and indexes, range must be always integer, so to convert a list to integer, use len to count before display. Note, list is using []
for i in range(len(supplies)):
    print(f"Index {i} in supplies is {supplies[i]}")
    
    '''Here the i(0 to n) will hold the len, converted to str, supplies as the list, listed as i'''


for a in range (len(cities)):
    print (f"I have live in {str(a)} on the following cities : {cities[a]} ")
