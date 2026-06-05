#display last two Records
import pandas as pd

df = pd.read_excel("student.xlsx")

print(df.tail(5))