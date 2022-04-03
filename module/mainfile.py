from itertools import product


def greet (message, name):
    return (f"{message}!{name}!How can i help you?")


def add (a , b):
    return (f"The sum of {a} and {b} is {int(a + b)}")


def types_of_backup(environment,export_type, productline):
    return f"{environment}.{export_type} {productline}.zip {productline}"
    

#print(__name__) #when you run this line, this will be equivalent to __main__
                #so in the if below,

if __name__ == "__main__":
    print(greet("Hi!","Ferdinand" ))

#1. A Function that will called in another file


