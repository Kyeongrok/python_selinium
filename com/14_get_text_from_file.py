file_name = "./save_line.txt"
f1 = open(file_name, encoding='utf-8')
lines = f1.readlines()

for line in lines:
    print(line)
