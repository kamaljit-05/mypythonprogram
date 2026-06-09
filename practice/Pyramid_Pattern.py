#Pyramid Pattern in Python
rows=int(input("enter the rows of pyramid"))
for i in range(1,rows+1,1): #outer loop
	for j in range (0,rows -i,1):#inner loop for space
		print(" ",end=" ")
	for k in range(1,2*i): #inner loop for stars
		print("*",end=" ")
	print()