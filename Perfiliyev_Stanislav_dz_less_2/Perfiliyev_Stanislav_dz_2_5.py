"""
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать,
как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию,
новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

"""

goods = [30, 52.4, 46, 35, 11, 17.3, 21.6, 45, 24, 31.8, 58, 62.5, 11.3, 79.2, 74, 75.3, 46.8, 11.4, 13, 17]


def pattern(list_name):
    number_format = ''
    for price in list_name:
        number_format += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
    return number_format

print(pattern(goods), id(goods))
goods.sort()
print(pattern(goods), id(goods))  # по возрастанию
cheapest = list(reversed(goods))
print(pattern(cheapest), id(cheapest))  # по убиванию
most_expensive = list(cheapest[:5])
print(pattern(most_expensive), id(most_expensive))  # самые дорогие
