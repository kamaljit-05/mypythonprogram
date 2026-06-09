#diamond  pattern in python
rows=int(input("enter the number of rows in python"))
for i in range(1,rows+1,1):
	for j in range(0,rows-i,1):
		print(" ",end=" ")
	for k  in range(1,2*i,1):
		print("*",end=" ")
	print()
for i in range(rows-1,0,-1):
	for j in range(0,rows-i,1):
		print(" ",end=" ")
	for k  in range(1,2*i,1):
		print("*",end=" ")
	print()