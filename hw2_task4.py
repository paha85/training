import random
list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
greetings = ['Салют,', 'Здравствуй,', 'Привет,', 'Рад видеть тебя,', 'Добрый день,']
names = []
for item in list:
    item = item.split()
    name = item.pop()
    names.append(name.capitalize())
print(names)
for name in names:
    print(f'{random.choice(greetings)} {name}!')