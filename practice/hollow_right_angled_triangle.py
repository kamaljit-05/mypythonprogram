#hollow right angled triangle pattern in python
rows=int(input("enter row size for the pattern"))
for i in range(1,rows+1,1):
	for j in range(1,i+1,1):
		if j==1 or i==rows or i==j:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()