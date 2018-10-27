import re
import pandas as pd

file_name = "./save_line.txt"
f1 = open(file_name, encoding='utf-8')
lines = f1.readlines()

replaced_lines = [re.sub(r'[가-힇]', '', line) for line in lines]
df = pd.DataFrame(replaced_lines)

# writer = pd.ExcelWriter("pdxl_c.xlsx", engine = 'openpyxl')
# df.to_excel(writer, sheet_name="sheet1", header=False)
# writer.close()