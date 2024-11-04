words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута", 
}

words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать", 
}

words_hard   = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}

levels = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

lvl=0
answers = {}

print('Выберите уровень сложности')
print('Легкий, средний, сложный')
print()
lev = input()
if lev.lower() == 'легкий':
    words = words_easy
elif lev.lower() == 'средний':
    words = words_medium
elif lev.lower() == 'сложный':
    words = words_hard

for k,v in words.items():
    print(k)
    print(len(v))
    print(f'начинается на ', {v[0]})
    user_ans = input('Введите ответ: ')
    if user_ans == v:
        print(f'Верно! {k.capitalize()} это {v.capitalize()}')
        answers[k] = True
        lvl+=1
    else: 
        print(f'Неверно! Правильный ответ {v.capitalize()}')
        answers[k] = False


print('Правильные ответы: ')
for k,v in answers.items():
    if v == True:
        print(k)
print('Неправильные ответы: ')
for k,v in answers.items():
    if not v:
        print(k)

print(f'Ваш уровень - {levels[lvl]}')
