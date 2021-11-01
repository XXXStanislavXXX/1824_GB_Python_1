"""

Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""


import os


# |--my_project_7_1
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # задаем базовую директорию
sec_dir = os.path.join(BASE_DIR, 'my_project_7_1')  # создаем в ней директорию в которой будут наши "папки"
third_dir = ['settings', 'mainapp', 'adminapp', 'authapp']  # создаем сами папки
for _ in third_dir:
    start = os.path.join(sec_dir, _)
    os.makedirs(start, exist_ok=True)


print('end')
