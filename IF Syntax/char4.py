#convert lower case to upper case
import sys
print("enter a lower char")
ch=input()
if len(ch)!=1:
	print("single digit allow")
	sys.exit()
if ch>="a" and ch<="z":
	x=ord(ch)-32
	print(chr(x))