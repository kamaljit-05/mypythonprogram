#Example 2: Derived class with its own constructor (no super())
class A:
	def __init__(self):
		print("A construtor")
class B(A):
	def __init__(self):
		print("B constructor")
ob=B()