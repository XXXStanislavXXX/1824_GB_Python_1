"""

Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html


Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.


"""

import os
import shutil
from custom_exceptions import FuncAttributeFailError


def crt_fun(dict, path, ext='py', par='w', folder='None'):
    """

    :param dict: {'директория1':[название файла,...], 'директория2': [...], ... }
    :param path: путь к файлу или дирректории
    :param ext: расширение
    :param par: операция='w' - запись/ опреация='с' - копия
    :param folder: только для параметра копия - директория, куда копируем
    :return: None

    """

    for _ in dict:  # Задание 7_2
        launcher = os.path.join(path, _)
        os.makedirs(launcher, exist_ok=True)
        for _ in dict[_]:
            if par == 'w':
                with open(os.path.join(launcher, f'{_}.{ext}'), 'w') as f:
                    f.write('')
            elif par == 'c':
                g = os.path.join(launcher, f'{_}.{ext}')
                shutil.copy2(g, folder)
            elif par != 'c':
                raise FuncAttributeFailError(f'{par} = c')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # базовая директория
second_dir = os.path.join(BASE_DIR, 'my_project_7_3')  # директория второго эшелона
third_dir = {'settings': ['__init__', ' dev', 'prod'],  # директории третьего эшелона
             'mainapp': ['__init__', 'models', 'views'],
             'authapp': ['__init__', 'models', 'views']}

comm_dir2 = os.path.join(BASE_DIR, 'my_project_7_3\\mainapp\\templates')
sub_dir2 = {'mainapp': ['base', 'index']}

comm_dir3 = os.path.join(BASE_DIR, 'my_project_7_3\\authapp\\templates')
sub_dir3 = {'authapp': ['base', 'index']}
try:
    crt_fun(third_dir, second_dir)
    crt_fun(sub_dir2, comm_dir2, 'html')
    crt_fun(sub_dir3, comm_dir3, 'html')
except (TypeError, SyntaxError, NameError) as _:  # отлавливаем ошибки
    print(f'concrete error mk_fun(): {_}')
except OSError as _:
    print(f'global error mk_fun(): {_}')


copy_dir = os.path.join(BASE_DIR, 'my_project_7_3\\templates')  # вкладываем .hthml
copy_dir1 = os.path.join(BASE_DIR, 'my_project_7_3\\templates\\mainapp')
copy_dir2 = os.path.join(BASE_DIR, 'my_project_7_3\\templates\\authapp')

sub_copy = ['mainapp', 'authapp']
for i in sub_copy:
    folder = os.path.join(copy_dir, i)
    try:
        os.makedirs(folder)
    except FileExistsError as _:
        print(f'makedirs error: {_}')
        break

try:
    crt_fun(sub_dir2, comm_dir2, 'html', 'c', copy_dir1)
    crt_fun(sub_dir3, comm_dir3, 'html', 'c', copy_dir2)
except (TypeError, SyntaxError, NameError) as _:
    print(f'concrete error mk_fun(): {_}')
except OSError as _:
    print(f'global error mk_fun(): {_}')
except FuncAttributeFailError as _:
    print(f'FuncAttributeFailError: {_}')

print('end')
