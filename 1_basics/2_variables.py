x = 5
y = "John"
print(x)
print(y)

print(type(x)) # type() is use to check the type of variables
print(type(y))


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = '3'
y = int(x)
print(type(x), type(y))


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# a, b, c = "daexport", "dbexport", "cdexport" # Many Values to Multiple Variables
# choice = input("enter your command choice: ")
# if choice == 'a':
#     print(a)
# elif choice == 'b':
#     print(b)
# elif choice == 'c':
#     print(c)
# else:
#     print("invalid")

#Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("===========")
print(x)
print(y)
print(z)
