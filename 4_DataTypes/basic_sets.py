from common_vars import food_set


#print the set
print(food_set)

#validating if exist
print('rice' in food_set)

#intersect (what's common between sets)
indian_food = {'curry','shawarma','bread'}
print(food_set.intersection(indian_food))

#difference ()
print(food_set.difference(indian_food))

#combine
print(food_set.union(indian_food))
