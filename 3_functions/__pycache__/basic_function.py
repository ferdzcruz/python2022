def hello_world() -> str:
    """Message to user"""
    print("Hello World\n")


#with variable
def hello(name) -> str:
    """Message to user"""
    return f"{name}!Hello World\n"


#Call a function
hello_world()


#pass in variable
name = 'ferdie'
print(hello(name))

# too add to a value
def add_10(num):
    return num + 10

print(add_10(10))

