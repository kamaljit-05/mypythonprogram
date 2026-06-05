#display data sheet wise
import pandas as pd

all_sheets = pd.read_excel("student.xlsx", sheet_name=None)

for sheet_name, data in all_sheets.items():
    print("Sheet:", sheet_name)
    print(data)