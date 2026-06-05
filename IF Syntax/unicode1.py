#display upper case,lower case,number
import sys
print("enter a char")
ch=input()
if len(ch)!=1:
    print("single value is allow")
    sys.exit()
print(ord(ch))
if ch>="A" and ch<="Z":
    print("upper case")
if ch>="a" and ch<="z":
    print("lower case")
if ch>="0" and ch<="9":
    print("number")
