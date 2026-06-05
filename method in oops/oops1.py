class square:
	def __init__(self):
		self.side=float(input("enter side of square"))
	def show(self):
		print("side of square=",self.side)
	def area(self):
		print("area of square=",self.side*self.side)
	def perimeter(self):
		return 4*(self.side)
s=square()
s.show()
s.area()
print("perimeter=",s.perimeter())
