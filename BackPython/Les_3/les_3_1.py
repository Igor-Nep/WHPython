letters_1 = ["A", "B", "C", "D"]
letters_2 = ["E", "F", "G", "K", "L", "M", "N"]

count = int(input())

letters_2_count = letters_2[:count]
letters_1.extend(letters_2_count)

# Не удаляйте код ниже, он нужен для проверки

print("".join(letters_1))