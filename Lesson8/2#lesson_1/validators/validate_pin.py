def check_pin(pin):
    count_pin=0
    for i in range(len(pin)):
        if pin[i].isdigit():
            count_pin+=1
    if count_pin >=4:
        return True
    else:
        return False 