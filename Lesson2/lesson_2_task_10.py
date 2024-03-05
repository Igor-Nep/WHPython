def bank(summ, time):
	for i in range(int(time)):
		summ = (float(summ) * 1.1)    
	return round(summ, 2)	 
	

summ = input('Введите вносимую сумму: ')
time = input('Введите количество лет для вклада: ')
itog = str(bank(summ,time))
print(f'Ваш итог по вкладу составит {itog} руб.')