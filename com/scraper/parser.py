import com.scraper.crawler as crawler
# parser -> text를 []로 만든다
# saver -> []를 excel로 저장한다

file_name = "./jolse_result.txt"
f1 = open(file_name, encoding='utf-8')
text = f1.read()

print(text)
