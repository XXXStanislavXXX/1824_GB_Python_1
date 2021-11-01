"""

Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat

*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

"""

from Perfiliyev_Stanislav_dz_7_1 import BASE_DIR, os
from collections import defaultdict
import django
import json  # для каталогов использовал Django , спасибо ребятам - подсказали


def compare(bulk):
    number = [10 ** n for n in range(1, 100)]
    for i in number:
        if 0 <= bulk <= i:
            return i


# comm_dir = django.__path__[0]
# comm_dir = os.path.join(BASE_DIR, 'some_data')
# comm_dir = os.path.join(BASE_DIR, 'my_project_7_3')
comm_dir = BASE_DIR  # 'C:\Users\User\Desktop\geek brains\Python_Homework\Perfiliyev_Stanislav_dz_less_7'

seven_files = defaultdict(list)
# тут все как в методичке

for root, dirs, files in os.walk(comm_dir):
    for _ in files:
        place = os.path.join(root, _)
        size = os.stat(place).st_size
        ext = _.rsplit('.', maxsplit=1)[-1].lower()
        seven_files[compare(size)].append(ext)

# для 7_4

my = {ext: (len(files)) for ext, files in sorted(seven_files.items())}
print(f'решение 7_4: \n{my}')
print()

# для 7_5

by = {ext: (len(files), list(set(files))) for ext, files in sorted(seven_files.items())}
print(f'Решение 7_5: \n{by}')

by_as_str = json.dumps(by)
with open('task_7_5_summary.json', 'w', encoding='utf-8') as _:
    _.write(by_as_str)

print('end')
