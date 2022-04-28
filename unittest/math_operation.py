#from vars import *

def add(x,y) -> int:
    """Add funtion"""
    return x + y

def subtract(x, y) -> int:
    '''Subtract funtion'''
    return x - y

def multiply(x, y) -> int:
    '''multiply funtion'''
    return x * y

def divide(x, y) -> int:
    '''divide funtion'''
    if y == 0:
        raise ValueError ("Cannot divide by zero") 
    return x / y

#def as function (x,y) are the variables inside the function
# if __name__ == '__main__':

#     print(add(num_x,num_y),add_mess)
#     print(subtract(num_x,num_y),sub_mess)
#     print(multiply(num_x,num_y),multiply_mess)
#     print(divide(num_x,num_y),divide_mess)
