
# calculation = 24
# name_of_unit = "hours"


# def days_to_unit(no_days): # put a variable with no value yet
#     #you will call the assign value here ex: no of days 
#     #return f"In {no_days} days, there are {no_days * calculation} {name_of_unit}"
#     print (f"In {no_days} days, there are {no_days * calculation} {name_of_unit}")
    

# no_of_days = input("enter no of days ")
# days_to_unit(int(no_of_days))


def function_that_prints():
    print ("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints() #this is not standard, from a function you should use return
f2 = function_that_returns()

#function_that_prints()

print ("Now let us see what the values of f1 and f2 are")
print (f1)
print (f2)


#when you print from a function, and assign to a variable, it will results to None
#when you return from a function, and assign to a variable, it will results to original value. So when you assign a value from 
# function, use return