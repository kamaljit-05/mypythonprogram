#student scoring Above average
import pandas as pd

df = pd.read_excel("student.xlsx")

avg = df["Marks"].mean()

print(df[df["Marks"] > avg])