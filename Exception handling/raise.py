class NegativeError(BaseException):
	def init(self):
		print("negative number not allow")
print("enter a number ")
no=int(input())
if no<0:
	try:
		raise NegativeError()
	except:
		print("exception caught negative number not allow ")
else:
	print("number=",no)

