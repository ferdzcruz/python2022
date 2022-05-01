# while True:
#     print("Enter username")
#     uname = input()
#     if uname != "ferdie":  #If input is ferdie, statement will continue to ask for username
#         continue 
#     print ("Hello, Ferdie! What is the password?") #it will ask for the password. If password is wrong, it will go back to the username
#     password = input()
#     if password == "Jesus":
#         break
# print("Thank you")



while True:
    print("Enter username")
    uname = input()
    if uname != "ferdie":  
        continue #continue will loop the statement until uname is ferdie
    print ("Hello, Ferdie! What is the password?")  #it will ask for the password. If password is wrong, it will go back to the username 
                                                    # due to while statement
    password = input()
    if password == "Jesus":
        break
print("Thank you")
