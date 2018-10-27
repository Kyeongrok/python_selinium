import re

file_name = "./save_line.txt"
f1 = open(file_name, encoding='utf-8')
lines = f1.readlines()

# save_line.txt에서 한글을 지우고 싶다.
# save_line에 있는 txt를 불러옴
#
for line in lines:
    print(re.sub(r'[가-힇]', '', line))





