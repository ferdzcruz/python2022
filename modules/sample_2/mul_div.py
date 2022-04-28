def multiply(x, y) -> int:
    '''multiply funtion'''
    return x * y

def divide(x, y) -> int:
    '''divide funtion'''
    if y == 0:
        raise ValueError ("Cannot divide by zero") 
    return x / y