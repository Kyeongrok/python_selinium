import xlwt
from datetime import datetime

today = datetime.today()


book = xlwt.Workbook(encoding='utf-8')
sheetName = str(today)[0:10]
sheet1 = book.add_sheet(sheetName)
sheet1.write(1, 1, 1)
sheet1.write(1, 2, 2)
sheet1.write(2, 1, 3)
sheet1.write(2, 2, 4)

book.save("bye.xls")