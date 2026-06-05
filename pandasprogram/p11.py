#Find avg marks
import pandas as pd

df = pd.read_excel("student.xlsx")

avg = df["Marks"].mean()

print("Average Marks =", avg)