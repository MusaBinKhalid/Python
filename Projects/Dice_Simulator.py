import random

while True:
    choice = input("Do you want to Roll the Dice (y/n): ")
    if choice.lower() == 'y':
        d1 = random.randint(0,6)
        d2 = random.randint(0,6)
        
        print(f"Dice 1: {d1}\nDice 2: {d2}")

    elif choice.lower() == 'n':
        print("Thanks for Playing!")
        break

    else:
        print("Invalid Choice!")
    