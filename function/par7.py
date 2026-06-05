# Calling with both positional and keyword arguments
def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display(1, 2, 3 ,"hi",name="Alice", age=30,city="bhu")
