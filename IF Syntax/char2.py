import sys
print("ener a char")
ch=input()
if len(ch)!=1:
    print("single value is allow")
    sys.exit()
if ch>='a' and ch<='z':
    print("lower case")