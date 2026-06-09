#hollow square patterrn
rows=int(input("enter the row size for the pattern"))
for i in range(1,rows+1,1): #outer loop for rows
	for j in range(1,rows+1,1): #inner loops for column
		if i==1 or i==rows or j==1 or j==rows: #print star only on borders
			print("*",end=" ")
		else:
			print(" ",end=" ") #print space inside 
	print()
'''Code Explanation:
1. We take input for the number of rows
to create a pattern in Python with a hollow square.

2. The outer loop runs through each row,
and the inner loop prints stars (*) only on the borders
(first/last row or column).

3. Inside the square, spaces (" ") 
are printed to maintain the hollow effect. 
Using end=" " keeps characters on the same line, 
while print() moves to the next row of the program.'''