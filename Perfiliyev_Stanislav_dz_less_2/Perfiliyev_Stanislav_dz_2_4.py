"""

Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка,
как привести их к корректному виду. Можно ли при этом не создавать новый список?

"""

data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

id(data)  # можно ли не создавая новый список

for name in data:

    # так как шагать будем с конца в начало => дадим умолчание '!', чтобы не дописывать к конечный принт

    change_name = '!'  # наша ' точка отсчета '
    name_to_change = name[::-1]  # определяем наше имя на замену
    for letter in name_to_change:  # вычленяем имя из билиберды
        change_name += letter
        if ord(letter) == 32:  # берем кракозябру до первого пробела с конца
            change_name = change_name[::-1]
            break

    print('Привет,' + change_name.title())  # итог
    print(id(data))  # можно ли не создавая новый список

# Шпаргалка

"""

ord_list = ' '
for number in ord_list:
    print(ord(number), end = " , ")

"""