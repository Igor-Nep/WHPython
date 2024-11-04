#1создание списков:
my_list = [item for item in range(1,10)]
print(my_list)
my_list_2 = [i for i in range(1,15)]
print(my_list_2)


#2увеличение каждого элемента списка на 1:
    #вместо этого:
items = [1,2,3]
items_plus = []
for item in items:
	items_plus.append(item + 1)
print(items_plus)
    #пишем это:        
items = [1,2,3]
items_plus = [item +1 for item in items]
print(items_plus)

#3преобразование типов:
    #вместо этого:
items = ["1", "2", "3"]
items_int = []
for item in items:
    items_int.append(int(item))
print(items_int)
    #пишем это:
items = ["1", "2", "3"]
items_int = [int(item) for item in items]
print(items_int)

#4фильтрация списков (вывод только положительных)
    #вместо этого:
numbers = [-2, -1, 0, 1, 2]
numbers_positive = []
for num in numbers:
    if num > 0:
        numbers_positive.append(num)
print(numbers_positive)
    #пишем это:
numbers = [-2, -1, 0, 1, 2]
numbers_positive = [num for num in numbers if num >0 ]
print(numbers_positive)

#Общая схема с условием выглядит так:

#[<что будет в списке> for <временная переменная> in <список> if <условие>]

#5вызов функуий (например модуля)
numbers = [-1, -2, -3]

[abs(num) for num in numbers]