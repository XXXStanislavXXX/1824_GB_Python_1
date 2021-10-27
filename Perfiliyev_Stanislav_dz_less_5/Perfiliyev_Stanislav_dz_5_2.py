"""

*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

"""


def odd_nums(n: int):  # задаем функцию
    odd_gen = (num for num in range(1, n + 1, 2))   # генератор
    print(type(odd_gen))  # доказываем, что генератор, это генератор)
    for n in range(1, n + 1, 2):
        print(next(odd_gen))  # не йелдим


end_number = input('Введите количество генерируемых чисел: ')  # нечетные числа от 1 до n
if end_number.isdigit():
    end_number = int(end_number)
    odd_nums(end_number)
else:
    print("введите цифровое значение")  # защита от дурака
