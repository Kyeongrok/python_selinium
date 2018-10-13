from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("../chrome/mac/chromedriver")

driver.get("http://dis.kofia.or.kr/websquare/index.jsp?w2xPath=/wq/fundann/DISMainFlucFund.xml&divisionId=MDIS01006002000000&serviceId=SDIS01006002000")
driver.implicitly_wait(10)

table = driver.title
print(table)
driver.implicitly_wait(10)

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

