"""

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение
компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

"""


class Warehouse:  # создаем нашу корзину
    pass


class Equipment:  # забиваем ее оборудованием
    def __init__(self, name, quantity, price, guarantee: bool, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.guarantee = guarantee
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.unit = {'Модель': self.name, 'Количество': self.quantity, 'Цена': self.price, 'Гарантия': self.guarantee}

    def __str__(self):  # задаем наш принт
        return f'{self.name}, {self.quantity}, {self.price}, {self.guarantee}'


    def accept(self):  # структура ввода данных
        try:
            unit_name = input(f'Модель: ')
            unit_quantity = int(input(f'Количество: '))
            unit_price = int(input(f'Цена: '))
            unit_guarantee = input(f'Гарантия: ')
            unit = {'Модель': unit_name, 'Количество': unit_quantity, 'Цена': unit_price, 'Гарантия': unit_guarantee}
            self.unit.update(unit)
            self.my_warehouse.append(self.unit)
            print(f'Список девайсов {self.my_warehouse}')
        except:
            return f'Ошибка'  # ошибка ввода

        print(f'Нажать Enter для продолжения, q для выхода')
        q = input(f'>>> ')
        if q == 'Q' or q == 'q':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'Все товары {self.my_warehouse_full}')
            return f'Выход'
        else:
            return Equipment.accept(self)

class Printer(Equipment):
    def print(self):
        return f'Указать кол-во {self.numb}'

class Scanner(Equipment):
    def scan(self):
        return f'Указать кол-во {self.numb}'

class Copier (Equipment):
    def copy(self):
        return f'Указать кол-во {self.numb}'


item_1 = Printer('epson', 4, 1000, True)
item_2 = Scanner('hp', 8, 2000, False)
item_3 = Copier('xerox', 16, 4000, True)
print(item_1.accept())
print(item_2.accept())
print(item_3.accept())
