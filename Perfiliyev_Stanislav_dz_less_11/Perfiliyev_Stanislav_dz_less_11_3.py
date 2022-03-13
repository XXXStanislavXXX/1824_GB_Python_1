"""

Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

"""


class My_Numeral_Exception:  # задаем исключение
    def __init__(self, *args):
        self.number_list = []

    def input_number(self):
        while True:
            try:
                val = int(input('Введите цифру: '))  # запрашиваем цифру
                self.number_list.append(val)
                print(f'Список {self.number_list} \n')
            except:
                print(f'Формат не верен')  # если ввели не цифру
                try_again = input(f'Хотите ввести снова? Введите Yes or No: ')  # даем "шанс исправится"

                if try_again == 'Yes' or try_again == 'yes':
                    print(exception.input_number())
                elif try_again == 'No' or try_again == 'no':
                    return f'Нет так нет!'
                else:
                    return f'Абырвагл! Пока!'


exception = My_Numeral_Exception()
print(exception.input_number())
