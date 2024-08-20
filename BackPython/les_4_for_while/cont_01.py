x = 10
while x:
    x = x - 1  # Либо x -= 1
    if x % 2 != 0: 
        continue # Нечетное? Тогда пропустить print
    print(x, end=' ')