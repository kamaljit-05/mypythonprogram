#display student name only
import pandas as pd

df = pd.read_excel("student.xlsx")

print(df["Name"])