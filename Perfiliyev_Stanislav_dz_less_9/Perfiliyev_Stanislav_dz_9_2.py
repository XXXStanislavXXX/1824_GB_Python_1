"""

Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в
1 см * число см толщины полотна;
проверить работу метода.

"""


class highway:  # задаем сам класс дороги с основными модулями (длинна, ширина и так далее)
    _length = None
    _width = None
    weight = None
    depth = None

    def __init__(self, length, width):  # задаем классовые элементы расхода (длинна, ширина)
        self.length = length
        self.width = width
        print('Введите спецификации: ')

    def _roadLaying(self):  # запрашиваем ввод глубины и ширины паралеллепипеда, калькулируем, выводим результат
        self.weight = int(input('Задайте высоту дороги цифрой: '))
        self.depth = int(input('Задайте глубину дороги цифрой: '))
        create = int(self.length * self.width * self.weight * self.depth / 1000)
        print(f'{create} тонн асфальта')


road = highway(int(input('Задайте длинну дороги цифрой: ')), int(input('Задайте ширину дороги цифрой: ')))
road._roadLaying()  # запускаем сам калькулятор