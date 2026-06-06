#global variable
a=10
class Demo:
    def __init__(self):
        print("global  variable=",a)
    def show(self,b):
        global a
        print("global variable =",a)
        a=30
def disp():
    print("global varaiable =",a)
ob=Demo()
disp()

ob.show(50)
print(a) 
a=50
print(a)
