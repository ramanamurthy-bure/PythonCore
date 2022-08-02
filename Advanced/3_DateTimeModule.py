import datetime

print("################################ (1 - datetime.time) ######################################")
mytime = datetime.time(2, 20)  # Here second will be considered as 00 as we did not pass
print(mytime)  # 02:20:00
print(mytime.hour)  # 2
print(mytime.minute)  # 20
print(mytime.second)  # 0
print(mytime.microsecond)  # 0

print("################################ (2 - datetime.time) ######################################")
mytime = datetime.time(3)  # Here if we did not specify anything it will be considered as 00
# Means, in the above line we only specified hour, so minute and second will be treated as 00
print(mytime)  # 03:00:00
print(mytime.hour)  # 3
print(mytime.minute)  # 0
print(mytime.second)  # 0
print(mytime.microsecond)  # 0

print("################################ (3 - datetime.time) ######################################")
mytime = datetime.time(4, 20, 23, 19)
print(mytime)  # 04:20:23.000019
print(mytime.hour)  # 4
print(mytime.minute)  # 20
print(mytime.second)  # 23
print(mytime.microsecond)  # 19

print("################################ (4 - datetime.date) ######################################")
today = datetime.date.today()
print(today)  # 2022-06-07
print(today.year)  # 2022
print(today.day)  # 7
print(today.month)  # 6
print(today.ctime())  # Tue Jun  7 00:00:00 2022

print("################################ (5 - datetime) ######################################")
from datetime import datetime

mydatetime = datetime(2021, 6, 7, 14, 20, 1)
print(mydatetime)  # 2021-06-07 14:20:01
# To update any attribute in date we can use the replace function like below
mydatetime = mydatetime.replace(year=2022)
mydatetime = mydatetime.replace(month=1)
mydatetime = mydatetime.replace(day=12)
print(mydatetime)  # 2022-01-12 14:20:01

print("################################ (6 - arithmetic operations on date ) ######################################")
from datetime import date

date1 = date(2022, 11, 3)
date2 = date(2021, 11, 3)
result = date1 - date2
print(type(result))  # <class 'datetime.timedelta'>
print(result)
print(result.days)
print(
    "################################ (7 - arithmetic operations on datetime ) ######################################")
date3 = datetime(2022, 11, 3, 11, 3, 40)
date4 = datetime(2021, 11, 3, 4, 5, 20)
result1 = date3 - date4
print(type(result1))  # <class 'datetime.timedelta'>
print(result1)
print(result1.days)
print(result1.seconds)
print(result1.total_seconds())
