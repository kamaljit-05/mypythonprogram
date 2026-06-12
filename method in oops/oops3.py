class simple_intrest:
	def __init__(self):
		self.principal=int(input("enter principal"))
		self.rate=int(input("enter rate "))
		self.time=int(input("enter time"))
	def si(self):
		print("simple intrest=",(self.principal*self.rate*self.time)/100)

simple_intrest().si()