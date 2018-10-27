import pandas as pd

def f(x):
    return x + 2

# type, list, function, parameter, return

list = [10, 20]
print(list)
print([10])
print(10)

print(["12", "22"])

print(type(10))
print(type("010"))

df1 = pd.DataFrame([12, 22])
writer = pd.ExcelWriter("./x_plus_2.xlsx", engine = 'openpyxl')
df1.to_excel(writer, sheet_name="sn", header=False)
writer.save()
writer.close()