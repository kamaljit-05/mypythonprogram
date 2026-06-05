#add new column in grade
import pandas as pd

df = pd.read_excel("student.xlsx")

df["Grade"] = "A"

print(df)