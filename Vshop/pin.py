def check_pin(pin):
    count_pin=0
    for i in range(len(pin)):
        if pin[i].isdigit():
            count_pin+=1
    if count_pin >=4:
        return True
    else:
        return False    



def assertion():
    try:
        assert check_pin('1234') == True
        assert check_pin("123") == False
        assert check_pin("a000") == False
        assert check_pin("0000") == True
    except AssertionError:
        print("Неверно, проверьте функцию на разных значениях")
    else:
        print("Все хорошо, все работает")

assertion()