from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def getPrice(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    result = urlopen(url)
    bs_obj = BeautifulSoup(result.read(), "html.parser")

    p_no_today = bs_obj.find("p", {"class":"no_today"})
    blind = p_no_today.find("span", {"class":"blind"})
    return blind.text

print(getPrice("015540"))