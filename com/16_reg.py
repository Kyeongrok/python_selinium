import re

target = '강ban가ana다라희'
target = re.sub(r'[가-힇]', '', target)
print(target)