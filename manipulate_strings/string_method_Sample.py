while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():
        break
    print('Please Enter a number for your age')


while True:
    print("Enter your password please")
    passwd = input()
    if passwd.isalnum():
        break
    print('Password should contain Alpa and Numberic')
