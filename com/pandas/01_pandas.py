import pandas as pd


values = [[1, 2], [3, 4]]
df1 = pd.DataFrame(values)

path = "pdxl.xlsx"
writer = pd.ExcelWriter(path, engine = 'openpyxl')
df1.to_excel(writer, sheet_name="sheet1", header=False)
writer.close()

