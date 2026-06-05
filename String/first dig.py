no=int(input("enter a number"))
if  no<0:
	no=-no
while no>=10:
	no=no//10
print("first digit=",no)