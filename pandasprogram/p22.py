''' add mark of three subject to the excel file
and then make new column of avg mark and 
display the avg mark of three subject '''
import pandas as pd
df = pd.read_excel("newstudent.xlsx")
df["Average"] = (df["Python"] + df["Java"] + df["SQL"]) / 3
print(df)
