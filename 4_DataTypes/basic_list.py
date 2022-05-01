#https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4

#list are mutable


from common_vars import courses, nums, lm_tables

print(courses[3])
print(courses[0:3])

#slicing
print(courses[:2])
print(courses[2:])

#Append in the end
courses.append('Art')
print(courses)

#insert to where you like
courses.insert(0,'Art')
print(courses)

#extend
courses_2 = ['Education','Filipino']
courses.extend(courses_2)
print(courses)

#remove
courses.remove('Filipino')
print(courses)

#pop is remove the last on the list
popped = courses.pop()
print(popped, courses)
popped = courses.pop()
print(popped, courses)

#sort
nums.sort()
print(nums)

#sort-reverse
nums.sort(reverse=True)
print(nums)

#sorted function
sorted_nums  = sorted(nums)
print(sorted_nums)

#min, max, sum
print(min(nums))
print(max(nums))
print(sum(nums))

#finding the index
print(courses.index('Art'))
print(courses.index('English'))

#in operator
print('Art' in courses)
print('Filipino' in courses)

#for statement
for item in courses:
    print(item)

#enumerate
for index,item in enumerate(courses):
    print(index,item)

#if you want to separate each item by comma
course_str = ' - '.join(courses)
#print(course_str)

#split
new_list = course_str.split(' - ')

print(course_str)
print(new_list)
