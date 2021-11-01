"""

Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
5: <class 'int'>


Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

a = calc_cube(5)
calc_cube(5: <class 'int'>)

"""

from functools import wraps


def logger(func):
    @wraps(func)
    def tralala(*args, **kwargs):
        result = []
        for it in args:
            try:
                print(f'{func.__name__}({it}: {type(it)})')
                result.append(func(it))
            except TypeError as err:
                print(f'{err}: "{it}"  is {type(it)}')
        for _, num in kwargs.items():
            try:
                print(f'{func.__name__}({num}: {type(num)})')
                result.append(func(num))
            except TypeError as err:
                print(f'{err} {num} type is {type(num)}')
        return result
    return tralala


@logger
def calc_five(x):
    return x ** 5


a = calc_five(5, '6', 6, g=3)
print(*a, sep=', ')
