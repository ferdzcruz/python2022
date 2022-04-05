import random,sys

def user_response(user_ans):

    if user_ans == 0:
        return 'yes'
    if user_ans == 1:
        return 'no'
    if user_ans == 2:
        return 'maybe'
    else:
        sys.exit()
    
    print("thank you.")

pc_response = random.randint(0,2)
user_ans = user_response(pc_response)
print(user_ans)



