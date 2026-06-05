def positive_negative(no1):
	if no1>0:
		print("number is positive")
	elif no1<0:
		print("number is negative")
	else:
		print("number is zero")
	return
print("enter a number")
no1=int(input())
positive_negative(no1)	