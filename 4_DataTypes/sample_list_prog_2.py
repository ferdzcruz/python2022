from tkinter.ttk import Separator


fruits = []
while True:
    print(f"Enter a fruit, {str(len(fruits) + 1)} or press ENTER to stop")
    food = input()
    
    if food == '':
        break
    fruits += [food]
    



fruits.insert (-1, 'and')
food = fruits
print(*food, sep=' ')


# separator = " "
# print(separator.join((map(str,food))))  #this will remove the bracket

# fruits.insert(-1,'and') # this will insert and in the before the last item
# for food in fruits:
#     print(food, end=' ') # this will print horizontally




