import random

print("🎲ROCK-PAPER-SCISSORS🎮")

while(1):

    computer = random.choice([1,2,3])

    player = int(input("\n1: Rock 🗻\n2: Paper 📃\n3: Scissors ✂\n\nEnter Your Choice: "))

    if player <= 3:
        gamedict = {1 : "Rock 🗻", 2 : "Paper 📃", 3 : "Scissors ✂"}

        print(f"\nYou Chose {gamedict[player]} and Computer Chose {gamedict[computer]}.")

        if computer == player:
            print("It's a Draw!")

        else: 
            if computer == 1  and player == 2:
                print("You Win 🎉")
            
            elif computer == 1 and player == 3:
                print("Computer Wins! 🎉")
            
            elif computer == 2 and player == 1:
                print("Computer Wins! 🎉")
            
            elif computer == 2 and player == 3:
                print("You Win 🎉")
            
            elif computer == 3 and player == 1:
                print("You Win 🎉")
            
            elif computer == 3 and player == 2:
                print("Computer Wins! 🎉")
   
    else:
        print("Enter Valid Choice!")        