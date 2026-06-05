#find the second Largest element in a list 
l=[5,8,12,4,7,12]
l.sort()
l.reverse()
for i in range(0,len(l)-1,1):
	if l[i]!=l[i+1]:
		break
print("second largest=",l[i+1])