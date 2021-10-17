"""

Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной
строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов

"""

last_number = 1
while last_number < 101:
    if last_number % 10 in range(5, 10):
        print(last_number, 'процентов')
    elif last_number % 10 == 0:
        print(last_number, 'процентов')
    elif 10 < last_number < 15:
        print(last_number, 'процентов')
    elif last_number % 10 == 1:
        print(last_number, 'процент')
    else:
        print(last_number, 'процента')
    last_number += 1
