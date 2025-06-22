def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n

x = int(input("Enter N: ")) 
print(sum(x))