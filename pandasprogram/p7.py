#display first three record
import pandas as pd

df = pd.read_excel("student.xlsx")

print(df.head(5))