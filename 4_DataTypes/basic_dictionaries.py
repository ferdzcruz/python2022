from multiprocessing.sharedctypes import Value
from common_vars import family

#how to call
print(family)
print(f"Ferdie's birthday is on {family['Ferdie']}")


#get method
print(family.get('Sophie')) #existing
print(family.get('bowee', 'Not Found')) #not existing

#add 
family['bowee'] = 'Dec 10'
print(family)

#update multiple
family.update({'Ferdie': 'July 17,1981', 'Jhoza': 'March 16,1984', 'Sophie': 'March 14,2013'})
print(family)

#delete
del family['bowee']
print(family)

#loop
print(len(family))
print(family.keys())
print(family.items())

for key, value in family.items():
    print(f"{key} - {value}")

