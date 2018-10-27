import pandas as pd
def save(list, fileName):
    df = pd.DataFrame(list)
    writer = pd.ExcelWriter(fileName, engine = 'openpyxl')
    df.to_excel(writer, sheet_name="sheet1", header=False)
    writer.close()
