#per object per instance variable
a=10 # global variable  
class Demo:
    def __init__(self):
        self.b=20  #instance variable
    def show(self):
        self.c=30   #instance variable
ob=Demo()
print(ob.__dict__)
ob.show()
print(ob.__dict__)
ob.d=40
print(ob.__dict__)
ob1=Demo()
print(ob1.__dict__)
ob1.x=50
print(ob1.__dict__)
