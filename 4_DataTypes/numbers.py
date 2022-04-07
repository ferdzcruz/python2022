import random
import sys
# a = 5 
# print (type(a))

# print(type(5.0))

# c = 5 + 3j
# print(c + 3)

# print(isinstance (a, complex))

#print(random.randrange(10,20))

x = ['a','b','c','d','e']
comp_entry = random.choice(x)


while True:
    print("Enter your guess: ")
    user_entry = input()
    if user_entry != comp_entry:
        print('wrong guess')
        continue
    if user_entry == 'q':
        sys.exit()
    else:
        print("Correct!")
        
   




