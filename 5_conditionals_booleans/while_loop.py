#while - as long as the condition is true

#1 this will print continuously
# while True:
#     print("Hellow World")

#2 While and break
# i = 0 #initial value, this will hold from 0
# while True:
#     print("Hellow World")
#     i = i + 1 #this will accumulate the value 0 + 1 = 1 + 1 = 2 + 1 = 3 ....
#     if i >= 5: #this will happen when it reach 5
#         break #this will break the loop after print

#3 While, continue, break

# while True:
#     uname = input("Enter username: ")
#     if uname != 'ferdie': #if it is not ferdie, it will continue on looping
#         continue          #because of the continue
#     else:                 #what if ferdie
#         break             #break or exit  


#4 we put another if within the statement

# while True:
#     uname = input("Enter username: ")
#     if uname != 'ferdie': #if it is not ferdie, it will continue on looping
#         continue          #because of the continue
#     upass = input("Enter password : ")
#     if upass == 'Jesus':  #if the password is Jesus, it will exit, if not, it will go back to uname. Why, because it's part of the while statement    
#         break             #break or exit
# print("Welcome")          #this will print once all condition are met  

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

print('bye')

