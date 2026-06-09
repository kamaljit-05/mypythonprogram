#Example 1: Derived class without its own constructor

class A:
	def __init__(self):
		print("A construtor")
class B(A):
	pass
ob=B()
