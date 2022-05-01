#if value is False,0, None, [] {} (), code will not executed, the rest will execute like True, 1
#False 0, 
# ==. > , < , >=, <=, !=, and , or

if 0:
    print("Hello World")

#True, not 0
if 1:
    print("Hello World")


#conditional simple if
score = 10
'''6 below = Fail, 7 to 9, pass, 10 excellent'''
# if score == 10:
#     print("Pass")

# if score >= 11:
#     print("wow")

# if score <= 9:
#     print('good job')

#conditional simple if with and operator, Nested if you use elif
if score > 7 and score <= 9: #between 7 to 9
    print("passed")
elif score == 10: # hightest
    print('Excellent')
elif score > 4  and score <= 6: #4 to 6 
     print('almost passed')
else:
    print('study more') # 3 and below

print('thank you') # This will print any output because it's not part of the if statement