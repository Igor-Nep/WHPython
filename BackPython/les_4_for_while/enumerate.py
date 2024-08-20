letters = ["A", "B", "C", "D", "E", "F"]
for i in range(len(letters)):
    letter = letters[i]
    print(i, letter)

#либо, с использованием enumerates в первую временную переменную попадает индекс (порядковый номер начиная с 0), а во вторую — значение
for i, letter in enumerate(letters):
  print(i, letter)

#можно задать стартовый индекс
for i, letter in enumerate(letters, start=1):
  print(i, letter)    


#с условием выводить только True
items = [True, True, False, True, True, False]

for index, value in enumerate(items, start=1):
   if value:
       print(index)  

#с условием выводит только четные элементы:
letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]

for i, letter in enumerate(letters, start=1):
    if i % 2 == 0: 
        print(i, letter)       