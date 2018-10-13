from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("../chrome/window/chromedriver.exe")

driver.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISMainFlucFund.xml&divisionId=MDIS01006002000000&serviceId=SDIS01006002000")
driver.implicitly_wait(10)

table = driver.title
print(table)
driver.implicitly_wait(50)

select = Select(driver.find_element_by_id('fundTyp_input_0'))

print(select)

# select by visible text
select.select_by_visible_text('주식형')
#
# # select by value
# select.select_by_value('1')

button = driver.find_element_by_css_selector("#btnSearImg")
# print(input)
button.click()
driver.implicitly_wait(50)
table = driver.find_element_by_class_name("grdMain_body_tbody")
print(table)
