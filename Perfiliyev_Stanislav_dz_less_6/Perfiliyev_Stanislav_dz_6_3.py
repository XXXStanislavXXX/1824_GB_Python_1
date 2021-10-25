"""

Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи

"""

import json
import sys
from itertools import zip_longest


def hobby(text):

    """
    обрабатываем текст и возвращаем список
    """

    return [row.strip().replace(',', ' ') for row in text]


with open('users.csv', 'r', encoding='utf-8') as f:
    nname = hobby(f)
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hob = hobby(f)
if len(hob) > len(nname):
    sys.exit(1)  # finished with exit code 1
d_v = dict(zip_longest(nname, hob[:len(nname)]))  # else задаём в словаре значение None

# encoder и запись словаря в файл

with open('task_6_3.py_dict.txt', 'w', encoding='utf-8') as fw:
    json.dump(d_v, fw, ensure_ascii=False)

# decoder читаем файл смотри тип

with open('task_6_3.py_dict.txt', 'r', encoding='utf-8') as fr:
    import_dict = json.load(fr)
    print(type(import_dict), import_dict)
