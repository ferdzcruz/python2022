
import random,sys

wins = 0
ties = 0
losses = 0

while True:
    print(f"{wins}{losses}{ties}")
    while True:
        print("Enter your move: [r] Rock, [s] Scissors, [p] Paper [q] quit")
        ply1 = input()
        if ply1 == 'q':
            sys.exit()
        if ply1 == 'r' or ply1 == 's' or ply1 == 'p':
            break
        print("type one of the following: r,p,s,q")

    if ply1 == 'r':
        print("Your move is Rock")
    elif ply1 == 's':
        print("Your move is Scissors")
    elif ply1 == 'p':
        print("Your move is Paper")

    random_num = random.randint(1,3)
    if random_num == 1:
        computer_move = 'r'
        print ("Computer move is Rock")

    elif random_num == 2:
        computer_move = 's'
        print ("Computer move is Scissor")

    elif random_num == 3:
        computer_move = 'p'
        print ("Computer move is Paper")

    if ply1 == 's' and computer_move == 's':
        ties = ties + 1
        print("it's a tie")
    
    if ply1 == 's' and computer_move == 'p':
        wins = wins + 1
        print("you win")
    
    if ply1 == 's' and computer_move == 'r':
        losses = losses + 1
        print("you lose")

    if ply1 == 'r' and computer_move == 'r':
        ties = ties + 1
        print("it's a tie")
    
    if ply1 == 'r' and computer_move == 's':
        wins = wins + 1
        print("you win")
    
    if ply1 == 'r' and computer_move == 'p':
        losses = losses + 1
        print("you lose")

    if ply1 == 'p' and computer_move == 'p':
        ties = ties + 1
        print("it's a tie")
    
    if ply1 == 'p' and computer_move == 's':
        wins = wins + 1
        print("you win")
    
    if ply1 == 'p' and computer_move == 'r':
        losses = losses + 1
        print("you lose")


   







    



for i in range(5):
    while True:
       
        
        computer_input(random_num)
        playermove = input()
        if playermove == 'r' and computer_input == 1:
            print("match")
        if playermove == 'r' and computer_input == 2:
            print("you win")


        




# if random_num == 1:r

#     print("rock")
# if random_num == 2:
#     print("scissor")
# if random_num == 3:
#     print("paper")


