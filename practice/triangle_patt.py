#right angled triangle pattern in python
rows= int(input("Enter the row size for the pattern"))
for i in range (1,rows+1,1):
	for j in range(1,i+1,1):
		print("*",end=" ")
	print()