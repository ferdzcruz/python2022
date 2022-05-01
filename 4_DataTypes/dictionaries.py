from common_vars import *
print(food_to_eat ['breakfast'])


for v in family.values():
    print(v)
print('\n')
for k in family.keys():
    print(k)
print('\n')
for i in family.items():
    print(i)
print('\n')

#get method
    #has value
print(f"I am bringing {str(picnicItems.get('cups',0))} cups")
print(f"I am bringing {str(picnicItems.get('apples',0))} apples")

    #not in the dictionary
print(f"I am bringing {str(picnicItems.get('eggs',0))} eggs")

#Nested Dictionary

allguest = {'Ferdie':{'bags':2, 'bike':1}}
for x in allguest['Ferdie'].keys():
    print(x)
for y in allguest['Ferdie'].values():
    print(y)

