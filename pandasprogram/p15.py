#sort student by marks
import pandas as pd

df = pd.read_excel("student.xlsx")

result = df.sort_values("Marks")

print(result)