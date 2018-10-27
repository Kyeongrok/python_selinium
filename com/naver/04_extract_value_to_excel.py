from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    result = urlopen(url)
    bs_obj = BeautifulSoup(result.read(), "html.parser")

    p_no_today = bs_obj.find("p", {"class":"no_today"})
    blind = p_no_today.find("span", {"class":"blind"})
    return blind.text

df1 = pd.DataFrame([
    [float(getPrice("015540").replace(",", ""))],
    [getPrice("207940")],
    [getPrice("068270")]
])
writer = pd.ExcelWriter("./naver_finance.xlsx", engine = 'openpyxl')
df1.to_excel(writer, sheet_name="sn", header=False)
writer.save()
writer.close()
