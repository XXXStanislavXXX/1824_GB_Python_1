"""

Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def costs(self):
        pass


class Coat:  # Задаем класс пальто
    def __init__(self, value):  # Задаем инициализатор
        self.v = value
        self.costs = round((self.v / 6.5 + 0.5), 1)

    @property
    def value(self):
        print('расход на пальто: ')  # задаем начальный принт
        return self.costs

    @value.setter
    def value(self, v):
        self.costs = round((v / 6.5 + 0.5), 1)  # Подсчитываем расход
        return self.costs

    def costs(self):
        pass


class Costume:
    def __init__(self, value):  # Задаем инициализатор
        self.h = value
        self.costs = round((2 * self.h + 0.3), 1)

    @property
    def value(self):
        print('расход на костюм: ')  # задаем начальный принт
        return self.costs

    @value.setter
    def value(self, h):
        self.costs = round((2 * h + 0.3), 1)  # Подсчитываем расход

    def costs(self):
        pass


class Clothes:
    def __init__(self, v, h):
        self.w = [Coat(v)] + [Costume(h)]

    def costs(self):
        combined_costs = 0
        for i in self.w:
            combined_costs += i.costs
        print('общий расход')
        return combined_costs


h = Clothes(12, 7)
c = Coat(12)
j = Costume(7)

print(c.value)
print(j.value)
print(h.costs())
print()

c.value = 3.3
j.value = 2.5
h = Clothes(3.3, 2.5)

print(j.value)
print(c.value)
print(h.costs())
