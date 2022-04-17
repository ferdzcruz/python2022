from common_vars import *

while True:
    print('Enter a name or (blank to stop)')
    name = input()

    if name == '':
        break
    
    if name in family:
        print(f"{family[name]} is the birthday of {name}")
    else:
        print('I dont recognize that name')
        print('What is their Birthday?')
        bday = input()
        print('Birthday database updated')
        
        

