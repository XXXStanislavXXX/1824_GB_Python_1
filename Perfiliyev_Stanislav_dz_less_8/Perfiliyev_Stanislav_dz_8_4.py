"""

Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?

"""
from functools import wraps


def value_check(func):  # проверка валидности значения
    @wraps(func)  # см. библу - ctrl + тык :-)
    def decor(*args):
        result = []
        for item in args:  # сама проверка
            try:
                if item > 0:
                    result.append(func(item))
                else:
                    raise ValueError(f'wrong val {item}')
            except TypeError as err:
                print(f'{err} {item} type is {type(item)}')
            return result
    return decor  # используем декор как проверку непосредственно значений


@value_check
def calc_five(x):
    return x ** 5


a = calc_five(5)
print(*a, sep=', ')

a = calc_five("asd")
print(*a, sep=', ')
