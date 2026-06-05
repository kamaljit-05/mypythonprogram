#student scoring above 80
import pandas as pd

df = pd.read_excel("student.xlsx")

result = df[df["Marks"] > 80]

print(result)