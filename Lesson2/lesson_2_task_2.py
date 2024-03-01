def is_year_leap(year):
    if int(year) % 4 == 0:
        return True
    else:
        return False

year = input('Введите год: ')

is_year_leap(year)
leap_t_f=is_year_leap(year)
print(f'Год {year}: {leap_t_f}')
