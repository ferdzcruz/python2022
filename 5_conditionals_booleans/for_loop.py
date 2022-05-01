
#For loop
#Range
# break and continue

# #1 using a list or tuple
# my_list = [1,2,3,4,5]
# for var in my_list:   #var will hold the value of my_list
#     print(var)


# #2 using range
# for var in range(10):
#     print(var)

# using specific position


food_set = {'egg','bread','rice','chicken','pork'}

for var in range (2, 5):  #starting point is 2, ending is 5 - 1 
    print(var)


for var in range (2, 10, 2):  #starting point is 2, ending is 10 - 1 , increament by 2
    print(var)

for food in food_set:
    if food == 'pork':
        print('Found')
        continue
    elif food == 'rice':
        break
    print(food)



#inner look

for my_food in food_set:
    print(my_food)

print(food_set)