x = 100  # Global

class Demo:
    company = "OpenAI"  # Class variable

    def __init__(self):
        self.name = "Kamaljit"  # Instance variable

    def show(self):
        y = 50  # Local variable
        print("Local:", y)
        print("Global:", x)
        print("Instance:", self.name)
        print("Class:", Demo.company)

obj = Demo()
obj.show()