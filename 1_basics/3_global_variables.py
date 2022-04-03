#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome" #global variable

# def myfunc():
#   print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)


print("===============================================")
x = "awesome"

def myfunc():
    global x
    x = "fantastic"



myfunc()

print("Python is " + x)
