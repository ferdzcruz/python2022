import os
# print('Hello World'[0:5])



# str1 = 'Hello world'
# #print(str1[start:end])
# print(str1[0:5])
# print(str1[:5]) #index from 0 to 5
# print(str1[:]) #all
# print(str1[::2]) # increamental
# print(str1[::-1]) #to reverse



# #Format
# old_story = "{0} is a good programmer. {0} is {1} years old. {0} loves to eat {2}"
# story = old_story.format('Ferdie',40,'inihaw')
# print(story)

# #Other format
# old_story = "{name} is a good programmer. {name} is {age} years old. {name} loves to eat {food}"
# story = old_story.format(name='Ferdie',age=40,food='inihaw')
# print(story)


# #format with input
# # m_name = input()
# # m_age = input()
# # m_location = input()
# # profile = "{name} is your name.{age} is your age. {loc} is your address."
# # print(profile.format(name=m_name,age=m_age,loc=m_location))

# #using f with try to pass on error
mess = "code error"
m_name = input()
m_age = input()
m_location = input()
try:
    print(f"{m_name} is your name.{age} is your age. {m_location} is your address.")
except NameError: print(mess)
