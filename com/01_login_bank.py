from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time


driver = webdriver.Chrome("../chrome/mac/chromedriver")
driver.implicitly_wait(30)

driver.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISMainFlucFund.xml&divisionId=MDIS01006002000000&serviceId=SDIS01006002000")

title = driver.title
print(title)

select = Select(driver.find_element_by_id('fundTyp_input_0'))

print(select)

# select by visible text
select.select_by_visible_text('혼합주식형')
#
# # select by value
# select.select_by_value('1')


button = driver.find_element_by_css_selector("#btnSearImg")
# print(input)
button.click()

time.sleep(10)
table = driver.find_element_by_css_selector("#grdMain")
print(table.text)

