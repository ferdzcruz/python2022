'''A list is value that contains multiple values in ordered sequence'''

name = ['ferdie','Josche','Sophie']
print(name[0])  #name is the name of the list
                #[0] is the index. This can only be integer


#concatinate
print(f"{name[0]} is the daddy, {name[1]} is the mommy, {name[2]} is the child")


#This ignore the index error since value is out of the range
try:
    print(name[4])
except IndexError: print("Not on the list")

try:
    print(name[1.0])
except TypeError: print("cannot be float")

#List also can contain other values

animals = [['coco','bowie'], ['rango','marvin']]
print(animals[0][1]) #index 0, with bowie as index 1 of index 0
print(animals[1][1])
print(f"{animals[0][0]} is a dog, {animals[1][0]} is a cat")

#count the number of the list
print(len(name),type(name))
print(len(animals),type(animals))

#Changing the values
animals[1][0] = 'muffin'
print(animals[1][0])


