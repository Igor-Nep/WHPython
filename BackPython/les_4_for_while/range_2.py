weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]

for i in range(0, len(weekdays)):
               if work[i] == True:
                 day='это рабочий день'
               elif work[i] == False:
                 day='это выходной день'
               print(f'{weekdays[i]} - {day}, а вечером {plans[i]}.')