empty_dict={}

footbal_sts = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": ['Австралия', 'Англия', 'Аргентина', 'Бельгия','еще 42 страны' ,'Эквадор', 'Япония'],
    "Награды": 
            {"Золотой мяч": "Лионель Месси", 
             "Серебрянный мяч": "Килиан Мбаппе",
             "Золотая бутса": "Килиан Мбаппе",
    "Больше всего голов" : {
        "Игрок": "Килиан Мбаппе - капитан команды",
        "Количество мячей": 8
    }, 

    }
}

def test_empty_dict():
    assert len(empty_dict) == 0

def test_read_value():
    count = footbal_sts["Число стран"]
    assert count == 48

def test_read_value2():
    country = footbal_sts["Страна"]
    assert country == 'Катар'

def test_write_value():
    footbal_sts["Число стран"] = 50 
    count = footbal_sts["Число стран"]
    assert count == 50 

def test_write_new():
    footbal_sts["Победитель"] = "Аргентина"
    win = footbal_sts["Победитель"]
    assert win == "Аргентина"  

def test_read_list():
    part = footbal_sts["Участники"]
    eng = footbal_sts["Участники"][1]
    assert len(part) > 0
    assert part[0] == "Австралия"
    assert eng == "Англия"

         