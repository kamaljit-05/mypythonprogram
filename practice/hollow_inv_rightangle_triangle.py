#hollow_inv_rightangle_triangle
rows=int(input("enter the size of rows"))
for i in range (rows,0,-1):
	for j in range(1,i+1,1):
		if j==1 or i==rows  or i==j:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
