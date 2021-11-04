"""

Реализуйте базовый класс Car. у класса должны быть следующие атрибуты:
speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""

import random


class Car:  # прописываем класс для тачек - функционал - движение\поворот\остановка

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = random.randint(0, 140)
        print(f'Скорость движения {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Остановка')

    def turn(self, direction: str):
        if self.speed > 30:
            print(f'Скорость на повороте {self.speed} км/ч')
        else:
            print(f'Поворот на {direction}')

    def show_speed(self):
        if self.speed == 0:
            print(f'Стоим')
        else:
            print(f'Скорость {self.speed} км/ч')


class TownCar(Car):  # прописываем класс городской тачки, родительским классом указываем класс тачек с функционалом

    def show_speed(self):
        if 0 < self.speed <= 60:
            print(f'Скорость {self.speed} км/ч')
        elif self.speed > 60:
            print(f'Превышаем! Скорость {self.speed} км/ч')
        else:
            print(f'Стоим')


class WorkCar(Car):  # тоже самое для рабочей машины

    def show_speed(self):
        if 0 < self.speed <= 40:
            print(f'Скорость {self.speed} км/ч')
        elif self.speed > 40:
            print(f'Превышаем! Скорость {self.speed} км/ч')
        else:
            print(f'Стоим')


class SportCar(Car):  # тоже самое для спорт кара
    color: str = 'желтый'
    name: str = 'Porsche Cayman'
    is_polise: bool = False


class PoliceCar(Car):  # ну и куда же без них)
    color: str = 'белый'
    name: str = 'LADA'
    is_polise: bool = True

    def show_speed(self):
        print(f'Со спецсигналами')


Volkswagen_polo = TownCar(50, 'красный', 'MINI', False)
Volkswagen_polo.go()
Volkswagen_polo.show_speed()
Volkswagen_polo.turn('лево')

Toyota_Corolla = TownCar(55, 'черный', 'Ford', False)
Toyota_Corolla.go()
Toyota_Corolla.show_speed()
Toyota_Corolla.turn('право')

Porsche_Cayman = SportCar(120, 'желтый', 'Dodge Charger', False)
Porsche_Cayman.go()
Porsche_Cayman.show_speed()
Porsche_Cayman.turn('лево')

LADA = PoliceCar(100, 'белый', 'BMW', True)
LADA.go()
LADA.show_speed()
LADA.turn('лево')
