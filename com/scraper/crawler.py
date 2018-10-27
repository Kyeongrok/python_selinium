import requests

# scraper -> text를 받아오는 것
def crawl(url):
    result = requests.get(url)
    return result.content