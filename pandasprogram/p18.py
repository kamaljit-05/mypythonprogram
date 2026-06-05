#find total number of students
import pandas as pd

df = pd.read_excel("student.xlsx")

print("Total Students =", len(df))