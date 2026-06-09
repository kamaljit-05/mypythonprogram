#inv pyramide patytern
rows = int(input("enter the rows of the pyramide"))
for i in range (rows,0,-1):
    for j in range(0,rows-i,1):
        print(" ",end=" ")
    for k in range(1,2*i,1):
        print("*",end=" ")
    print()
    