import sys, random

rannum = random.randint(1,20)


while True:
    print("I am thinking of a number 1 to 20.")
    response = input("Can you make a guess? ")
    if int(response) > rannum:
        print("your guess is high")
    if int(response) < rannum:
        print("your guess is low")
    if int(response) == rannum:
        break
    elif int(response) > 20:
        print("you're out of range.Goodbye")
        sys.exit()
        
print(f"your guess is correct!Hidden number is {rannum}")

        
