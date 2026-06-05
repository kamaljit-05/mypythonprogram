no=int(input("enter a number"))
s=0
temp=no
while no!=0:
	r=no%10
	s=r+s*10
	no=no//10
if temp==s:
	print("number is pd")
else:
	print("no is not pd")