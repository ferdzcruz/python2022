#Tuple are immutable

from common_vars import food

food_2 = (food)
print(food)
print(food_2)

food[0] = 'beef'
'''Tuple are immutable'''

print(food)
print(food_2)