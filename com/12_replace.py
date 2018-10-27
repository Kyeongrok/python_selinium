from datetime import datetime

today = datetime.today()

print("type:", type(today))
print(today)

sToday = str(today)
print("sToday:", sToday)
print("sToday type:", type(sToday))

replacedSToday = sToday.replace(":", "")
print(replacedSToday)
