#find lowest mark
import pandas as pd

df = pd.read_excel("student.xlsx")

print("Lowest Marks =", df["Marks"].min())