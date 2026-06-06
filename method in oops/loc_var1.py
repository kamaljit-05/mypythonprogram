# Local Variable
class Demo:
    def __init__(self):
        a=10
        print("local variable=",a)
    def show(self,b):
        e=40
        print("local or formal parameter =",b)
def disp():
    c=30
    print("local varaiable =",c)
ob=Demo()
disp()
ob.show(50)
