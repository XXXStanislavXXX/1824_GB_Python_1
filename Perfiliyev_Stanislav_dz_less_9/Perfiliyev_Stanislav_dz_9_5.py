"""

Реализовать класс Stationery (канцелярская принадлежность). определить в нём атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение; создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

"""


class Stationery:  # родительский класс
    title = None
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):  # Переопределение метода
        print('Ручка')


class Pencil(Stationery):
    def draw(self):  # Переопределение метода
        print('Карандаш')


class Handle(Stationery):
    def draw(self):  # Переопределение метода
        print('Маркер')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
