def evenodd(no):
	if no%2==0:
		return "even"
	else:
		return "odd"

print("enter a number")
no=int(input())	
print(evenodd(no))