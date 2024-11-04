import random
file = open('D:/Python312/git/WHPython/Lesson8/2#lesson_1/6_2files/test.txt', 'rt')
for line in file:
    print(line)
file.close()

with open('D:/Python312/git/WHPython/Lesson8/2#lesson_1/6_2files/test.txt', 'rt') as file:
    for line in file:
        print(line)
omm = ['temp', 'still', 'open', ' mit', 1, 5, 9, 10, 'm', 'f', 'w']

for i in range (0, 20):
    print(random.choice(omm))