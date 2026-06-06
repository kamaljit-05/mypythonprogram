class Calculator:
    def __init__(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter another number: "))

    def add(self):
        print("Addition =", self.num1 + self.num2)

    def sub(self):
        print("Subtraction =", self.num1 - self.num2)

    def mult(self):
        print("Multiplication =", self.num1 * self.num2)

    def div(self):
        if self.num2 == 0:
            print("Zero not allowed in denominator")
        else:
            print("Division =", self.num1 / self.num2)

calc = Calculator()

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        calc.add()
    elif choice == "2":
        calc.sub()
    elif choice == "3":
        calc.mult()
    elif choice == "4":
        calc.div()
    elif choice == "5":
        print("Exiting calculator. ")
        break
    else:
        print("Invalid choice. Please try again.")
