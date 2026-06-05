#display student with highest marks
import pandas as pd

df = pd.read_excel("student.xlsx")

result = df[df["Marks"] == df["Marks"].max()]

print(result)