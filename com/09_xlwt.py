import xlwt
from datetime import datetime

today = datetime.today()


book = xlwt.Workbook(encoding='utf-8')

# class = object(것)


sheetName = "2018-10-18"

print(type(sheetName))
print(type(today))

print("=>", str(today))
print("==>", type(str(today)))

sheetName = str(today)[0:10]
print(sheetName)
book.add_sheet(sheetName)

book.save("bye.xls")