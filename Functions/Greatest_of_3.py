def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f"{n1} is the Greatest")
    elif n2>n1 and n2>n3:
        print(f"{n2} is the Greatest")
    else:
        print(f"{n3} is the Greatest")

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
greatest(a,b,c)