#save Modified Data to new Excel File 
import pandas as pd

df = pd.read_excel("student.xlsx")

df["Grade"] = "A"

df.to_excel("newstudent.xlsx", index=False)

print("File Saved Successfully")
