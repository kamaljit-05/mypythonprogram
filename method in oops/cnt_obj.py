# count no of object 

class Demo:
    c=0# class variable
    def __init__(self):
        Demo.c=Demo.c+1
ob1=Demo()
ob2=Demo()
ob3=Demo()
L=[Demo(),Demo(),Demo()]
print("no of object=",Demo.c)

