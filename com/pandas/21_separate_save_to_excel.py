import re
import com.pandas.save_to_excel as ste

file_name = "./save_line.txt"
f1 = open(file_name, encoding='utf-8')
lines = f1.readlines()

replaced_lines = [re.sub(r'[가-힇]', '', line) for line in lines]

ste.save(replaced_lines, "pdxl_c.xlsx")
