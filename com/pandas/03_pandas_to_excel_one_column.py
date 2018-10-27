import pandas as pd


values = [[1], [3]]
df = pd.DataFrame(values)

path = "pdxl_c.xlsx"
writer = pd.ExcelWriter(path, engine = 'openpyxl')

print(df)

df.to_excel(writer, sheet_name="sheet1", header=False)
writer.close()

