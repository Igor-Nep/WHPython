deposit = 0
replenishment = int(input('Введите сумму: '))
while deposit < 12000:
    deposit += replenishment
    print(f"Баланс счета = {deposit}")