def month_to_season(n):
	m=int(n)
	if m == 1 or m == 2 or m == 12:
		return 'Зима'
	elif m == 3 or m == 4 or m == 5:
		return 'Весна'
	elif m in [6, 7, 8]:
		return 'Осень' 
	else: 
		return 'Введите число от 1 до 12'	
				
		
n=input('Введите номер месяца: ')
result = (month_to_season(n))	
print(result)	
