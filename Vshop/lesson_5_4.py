def remove_from_string(string, *symbols_to_remove):
    """
    Удаляем символы перечисленные после первого аргумена
    """
    for symbol in symbols_to_remove:
        string = string.replace(symbol,'')
    return string
print(remove_from_string.__doc__)