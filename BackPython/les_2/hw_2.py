import time
import os 
bals = 0
print('Привет! Предлагаю проверить свои знания английского!\nНапиши как тебя зовут: ')
name = input()
print(f'Привет, {name}, начинаем тренировку!')
time.sleep(5)
os.system('cls')
print('Вопрос 1:')
print('My name ___ Vova.')
ans_1 = input('Какое слово пропущено?: ')
if ans_1.upper() == 'IS':
    print('Верно!\nПолучаешь 10 баллов!')
    bals += 10
else:
    print('Неверно!\nПолучаешь 0 баллов!')

time.sleep(3)
os.system('cls') 
print('Вопрос 2:')
print('I ___ a coder')
ans_2 = input('Какое слово пропущено?: ')   
if ans_2.upper() == 'AM':
    print('Верно!\nТы получаешь 10 баллов')
    bals += 10
else:
    print('Неверно!\nПолучаешь 0 баллов!')

time.sleep(3)
os.system('cls')
print('Вопрос 3:')
print('I live ___ Moscow')
ans_3 = input('Какое слово пропущено?: ')
if ans_3.upper() == 'IN':
    print('Верно!\nТы заработал 10 баллов!')
    bals += 10
else:
    print('Неверно!\nТы не зарабатываешь баллы!')

time.sleep(3)
os.system('cls')
print(f'Ну вот, {name}, закончился тест.')
time.sleep(2)
print(f'Ты верно ответил на {int(bals/10)} вопросов из трёх')
print(f'Ты заработал {bals} баллов')
print(f'Это {int(bals/30*100)} % верных ответов')