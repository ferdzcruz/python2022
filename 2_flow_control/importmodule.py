import random
import sys

for i in range(10):
    print(random.randint(0,10))


while True:
    print("Type exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print(f"your response is {response}.")

    