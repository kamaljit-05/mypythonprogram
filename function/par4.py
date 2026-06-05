def multiply(*arg):
	result=1
	for num in arg:
		result*=num
	return result
print(multiply(2,3))