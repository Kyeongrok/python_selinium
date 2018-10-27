from datetime import datetime
from selenium import webdriver
import time
import xlwt
import re

driver = webdriver.Chrome("../chrome/mac/chromedriver")
driver.get("http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/startest/BISBndSrtPrcDay.xml&divisionId=MBIS01070010000000&divisionNm=%25EC%259D%25BC%25EC%259E%2590%25EB%25B3%2584&tabIdx=1&w2xHome=/xml/&w2xDocumentRoot=")

title = driver.title

time.sleep(1)
button = driver.find_element_by_css_selector("#image1")
button.click()

time.sleep(1)
table = driver.find_element_by_css_selector("#grdMain_body_tbody")

text = table.text

file_name = "./save_line.txt"
f1 = open(file_name, mode='w+', encoding='utf-8')
f1.write(str(text))

regex = r'[가-힇]+'
hangul = re.findall(regex, text)
sHangul = str(hangul)

sText = str(text)

for i in sHangul:
    sText.replace(i,"")

replacedtext = sText.replace("-","")

book = xlwt.Workbook(encoding="utf-8")

today = datetime.today()

def get_today():
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    return s
sheetName = str(today).replace(":","")[0:10]

sheet1 = book.add_sheet(sheetName)

list = replacedtext.split("\n")

for num in range(0, len(list)):
    sheet1.write(num, 0, list[num])

book.save("./Python_Kofiabond.xls")


driver.close()



