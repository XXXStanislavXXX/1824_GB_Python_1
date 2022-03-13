"""

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.

"""

class Complex_Number:  # задаем наше комплексное число
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b'

    def __add__(self, other):  # задаем логику сложения
        return f'z = {self.a + other.a + self.b + other.b}'

    def __mul__(self, other):  # задаем логику умножения
        return f'z = {self.a * other.a * self.b * other.a}'

    def __str__(self):  # задаем наш "принт"
        return f'z = {self.a} + {self.b}'


zet = Complex_Number(3, 5)  # задаем наши числа а
zed = Complex_Number(2, 4)  # задаем наши числа b
print(zet + zed)
print(zet * zed)
