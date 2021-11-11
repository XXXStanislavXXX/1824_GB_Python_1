"""

Реализовать базовый класс Worker (работник). Определить атрибуты:
name, surname, position (должность), income (доход); последний атрибут должен быть защищённым и
ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера
на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров.

"""


income = {'wage': 123456789, 'bonus': 987654}  # словарь  с окладом и премией


class Worker:  # класс сотрудника

    def __init__(self, name: str, surename: str, position: str, income: dict):
        self.name = name.title()
        self.surname = surename.title()
        self.position = position
        self._income = income

class Position(Worker):  # подкласс сотрудника

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker = Position(input('Введите ваше имя:'), input('Введите вашу фамилию: '), input('Введите вашу позицию: '), income)
# проверка работы, через должность со вводом данных ссылка на класс Рабочий через класс позиция

print(worker.get_full_name(), worker.get_total_income())
