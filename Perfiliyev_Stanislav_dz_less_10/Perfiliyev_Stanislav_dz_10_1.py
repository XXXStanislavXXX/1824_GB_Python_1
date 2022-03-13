"""

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.

"""

from operator import add


class Matrix:  # Задаем класс Матрица
    def __init__(self, new_matrix: list):  # Задаем инициализатор? забыл как он правильно называется)
        # Но инициализирует объект с заданными параметрами
        self.new_matrix = new_matrix

    def __str__(self):
        return self.matrix_result(self.new_matrix)  # Задаем метод вывода матрицы значений

    def __add__(self, other):  # Задаем метод сложения
        _list = []
        for i in range(len(self.new_matrix)):
            _list.append(list(map(add, self.new_matrix[i], other.new_matrix[i])))
        return self.matrix_result(_list)

    def matrix_result(self, m):  # итоговая функция вывода
        self.m = m
        _str = ''
        for i in m:
            _str += f"|{', '.join(map(str, i))}|\n"
        return _str


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

b = [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]

m1 = Matrix(a)
m2 = Matrix(b)
print(m1)
print(m2)
print(m1 + m2)