from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("../chrome/mac/chromedriver")
driver.get("http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/startest/BISBndSrtPrcDay.xml&divisionId=MBIS01070010000000&divisionNm=%25EC%259D%25BC%25EC%259E%2590%25EB%25B3%2584&tabIdx=1&w2xHome=/xml/&w2xDocumentRoot=")

title = driver.title
print(title)

time.sleep(1)
driver.find_element_by_css_selector("#srchDt_input").clear()
input = driver.find_element_by_css_selector("#srchDt_input").send_keys("20181011")


time.sleep(1)
button = driver.find_element_by_css_selector("#image1")
button.click()

time.sleep(1)
table = driver.find_element_by_css_selector("#grdMain_body_tbody")

text = table.text

import xlwt

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet2")

list = text.split("\n")

for num in range(0, len(list)):
    sheet1.write(num, 0, list[num])

book.save("hello2.xls")



