from datetime import datetime

thedate = datetime(1986, 4, 26, 1, 23, 47) # 26 апреля 1986 01:23:47

print("Год", thedate.year)
print("Месяц", thedate.month)
print("День", thedate.day)
print("Час", thedate.hour)
print("Минута", thedate.minute)
print("Секунда", thedate.second)

# Выведет

from datetime import datetime

thedate = datetime.now()

print(thedate)

from datetime import date

thedate = date.fromisoformat("2021-05-04")

print(thedate.year)
print(thedate.month)
print(thedate.day)

#Форматирование даты

from datetime import date

thedate = date(1970, 1, 5)

date_formatted = thedate.strftime("%d %B %Y ") # День Месяц Год

print(date_formatted)

# Выведет 05 January 1970