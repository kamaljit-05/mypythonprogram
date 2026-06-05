#find highest mark
import pandas as pd

df = pd.read_excel("student.xlsx")

print("Highest Marks =", df["Marks"].max())