catNames = [] # initial value set to null

while True : #for looping until it breaks:
    print(f"Enter the name of the person {str(len(catNames) + 1)} (Or Enter nothing to stop)") # catnames to list > int + 1 > string
    name = input() # user input
    if name == '': #to stop, meaning no value
        break
    catNames = catNames + [name]
print("The person's names are :")
for name in catNames:
    print(' ' + name)
