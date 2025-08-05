import random

while(True):
    choice = input("Do you want to Roll the Die (Y/N): ").lower()

    if choice == 'y':
        d1 = random.randint(1,6)

        if d1 == 1:
            print("\n   *   \n")
        elif d1 == 2:
            print("      *\n       \n*      ")
        elif d1 == 3:
            print("      *\n   *   \n*      ")
        elif d1 == 4:
            print("*     *\n       \n*     *")
        elif d1 == 4:
            print("*     *\n   *   \n*     *")
        elif d1 == 6:
            print("*     *\n*     *\n*     *")

    elif choice == 'n':
        print("Thanks for Playing")
        break

    else:
        print("Enter Valid Choice!")