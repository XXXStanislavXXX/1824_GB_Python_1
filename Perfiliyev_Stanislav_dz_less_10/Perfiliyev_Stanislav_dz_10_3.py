"""

Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до
целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****

"""


class Unit:  # Задаем класс
    def __init__(self, integer):  # Определяем инициализатор
        self.integer = int(integer)

    def __str__(self):  # Определяем метод вывода
        return f'{self.integer * "* "}'

    def __add__(self, other):  # Определяем метод сложения
        return Unit(self.integer + other.integer)

    def __sub__(self, other):  # Определяем метод вычитания
        return Unit(self.integer - other.integer)

    def __mul__(self, other):  # Определяем метод умножения
        return Unit(int(self.integer * other.integer))

    def __truediv__(self, other):  # Определяем метод деления
        return Unit(round(self.integer / other.integer))

    def make_order(self, _rows):  # Разбили аргумент по строкам
        s = ''
        i = int(self.integer / _rows)
        for _ in range(i):
            s += f'{"* " * _rows}\\n'
        s += f'{"* " * (self.integer % _rows)}'
        return s


c1 = Unit(10)
c2 = Unit(13)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(3))
print(c2.make_order(3))
