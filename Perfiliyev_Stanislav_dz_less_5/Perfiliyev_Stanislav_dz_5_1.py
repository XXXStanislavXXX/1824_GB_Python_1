"""

Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...


"""


import sys


n = 15
odd_gen = (num for num in range(1, n + 1, 2))  # сам генератор
print(next(odd_gen), next(odd_gen), next(odd_gen), sep=', ')
print(type(odd_gen))  # доказываем, что написали именно генератор


def nums_gen(start, end):
    for num in range(start, end + 1, 2):
        yield num  # реализация yield


nums_list = nums_gen(1, n + 1)
print(*nums_list, sep=', ')
