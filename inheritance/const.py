class A:
	def __init__(self,x):
		self.x=x
	def dispA(self):
		print(self.x)
class B(A):
	def __init__(self,x,y):
		super().__init__(x)
		self.y=y
	def dispB(self):
		print(self.y)
ob=B(10,20)
ob.dispA()
ob.dispB()
obj=B(30,40)
obj.dispA()
obj.dispB()