'''wap take salary from  keyboad if salary>=5000 da=30% hra=20%  if salary <5000 
da=20% hra=10% then display basic salary da hra and totalsal'''

print("enter the salary")
sal=int(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
print("da=",da,"hra=",hra)
print("total salary=",sal+da+hra)