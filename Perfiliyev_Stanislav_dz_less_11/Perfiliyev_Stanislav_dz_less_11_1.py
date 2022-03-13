"""

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""


class Number(int):
    def __str__(self):
        return f"{self:02}"


"""

выводит дату представленную в виде кортежа целых чисел dd, mm, yyyy. Год считается валидным начиная с 1970
param date: кортеж (dd, mm, yyyy)
return: bool результат проверки, неверное число элементов в кортеже при распаковке приведет к ValueError

"""


class Date:  # Задаем класс и вводные
    date = ('day', 'month', 'year')

    def __init__(self, data: str):  # задаем интерпретатор с возбуждением ошибки не валидности
        day, month, year = self.separate(data.split('.'))

        if not self.valid(day, month, year):
            raise ValueError(f'{data} ошибка формата даты')

        self.day = day
        self.month = month
        self.year = year

    def __iter__(self):
        for d in self.date:
            yield self.__getattribute__(d)

    @classmethod  # наш декоратор
    def separate(cls, data):
        return [Number(d) for d in data]

    @staticmethod  # второй декоратор
    def valid(*data):
        if not all(map(lambda x: isinstance(x, int), data)):
            return False

        day, month, year = data
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1900])

    def __str__(self):  # формат нашего "принта"
        return f"Дата '{'.'.join([str(j) for j in self])}'"


if __name__ == '__main__':
    try:
        print(Date('22.2.1990'))
    except ValueError as error:
        print(error)
