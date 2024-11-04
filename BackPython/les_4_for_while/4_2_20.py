books = {
   "Саймон Сингх": "Книга шифров",
   "Брюс Шнайер": "Практическая криптография",
   "Нил Стивенсон": "Криптономикон",
   "Дэвид Кан": "Взломщики кодов",
   "Альбрехт Бойтельспахер": "Криптология",
}
book = []
author = []
b_a = {}

for k,v in books.items():
  book.append(v)
  author.append(k)
  b_a[k] = v
print('-')
print('Книги:')
for i in book:
  print(i)
print('-')
print('Авторы:')
for i in author:
  print(i)
print('-')
print('Библиотека:')
for i,n in b_a.items():
  print(f'{i} - {n}')