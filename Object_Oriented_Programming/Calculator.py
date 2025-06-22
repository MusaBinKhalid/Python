class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square is {self.n * self.n}")

    def cube(self):
        print(f"The Cube Root is {self.n * self.n * self.n}")

    def sqrt(self):
        print(f"The Square Root is {self.n ** (1/2)}")

a = Calculator(int(input("Enter a Number: ")))
a.square()
a.cube()
a.sqrt()

