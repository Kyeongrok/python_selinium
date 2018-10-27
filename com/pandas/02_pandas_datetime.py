import pandas as pd


randomValues = [["2018-10-17", 2], [3, 4]]
df1 = pd.DataFrame(randomValues)

path = "pdxl.xlsx"
writer = pd.ExcelWriter(path, engine = 'openpyxl')

df1.to_excel(writer, sheet_name="sheet1", header=False)
writer.save()
writer.close()

