#вывод наибольшего по длине списка с неограниченным количеством аргументов
def longest_list(*lists):
    leader = []
    for list_ in lists:
        if len(list_) > len(leader):
            leader = list_
    return leader

print(longest_list([1], [1,2,3], [1,4,5,6,7,8]))  

#удаляем символ из строки
def remove_from_string(string, *symbols_to_remove):
    for symbol in symbols_to_remove:
        string = string.replace(symbol,'')
    return string    

print(remove_from_string('Oh, look i just have understand a peace of Python!','!'))