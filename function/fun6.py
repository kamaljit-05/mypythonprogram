def SI():
	print("enter the principal")
	p=int(input())
	print("enter the rate")
	r=int(input())
	print("enter time period")
	t=int(input())
	si=(p*r*t)/100
	return si
Si=SI()
print("simple interst=",Si)