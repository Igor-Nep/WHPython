import math
def square(a):
    sq = math.ceil(float(a)) * math.ceil(float(a))
    return sq

st = input('Введите длину стороны: ')
square(st)
sq = square(st)
print('Площадь: ' + str(sq))
