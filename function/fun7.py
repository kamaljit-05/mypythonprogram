def SI(p,r,t):
	si=(p*r*t)/100
	return si
print("enter the principal value")
p=int(input())
print("enter the rate")
r=int(input())
print("enter the time period")
t=int(input())
Si=SI(p,r,t)
print("simple interst",Si)