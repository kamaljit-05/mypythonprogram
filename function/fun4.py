#return value with no argument   add two number
def add():
	print("enter a number")
	no1=int(input())
	print("enter another number")
	no2=int(input())
	s=no1+no2
	return s
ADD=add()
print("addition=",ADD)
