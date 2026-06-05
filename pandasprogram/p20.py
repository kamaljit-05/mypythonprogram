#display city-wise students
import pandas as pd

df = pd.read_excel("student.xlsx")

print(df.groupby("City").size())