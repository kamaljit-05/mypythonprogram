import pandas as pd
data={
	"Name":["navin","rahul"],
	"age":[16,17]
}
df=pd.DataFrame(data)
#write to Excel
df.to_excel("student.xlsx",index=False)
#read from Excel
df2=pd.read_excel("student.xlsx")
print(df2)