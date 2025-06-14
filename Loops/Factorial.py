num = int(input("Enter a Number: "))
fact = 1

while(num>1):
    fact = fact * num
    num = num - 1 

print(f"Factorial is {fact}")
