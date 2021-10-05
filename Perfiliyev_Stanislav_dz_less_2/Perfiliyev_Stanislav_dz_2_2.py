"""

Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
чисел со знаком? result = [x for x in condition if type(x) != str]
print(result)

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
дополнить числа до двух разрядов нулём!

"""

# задаем переменную списка
condition = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
condition.reverse()
for value in condition:
    if ord(value[-1]) in range(48, 58):
        condition.insert((condition.index(value) + 1), '"')
condition.reverse()
for value in condition:
    if ord(value[-1]) in range(48, 58):
        condition.insert((condition.index(value) + 1), '"')
for value in condition:
    if ord(value[0]) == 43 or ord(value[0]) == 45:
        new = int(value[1:])
        new_value = '{:02d}'.format(new)
        index = condition.index(value)
        condition[index] = value[:1] + new_value
for value in condition:
    if ord(value[0]) in range(48, 58):
        new = int(value)
        new_value = '{:02d}'.format(new)
        index = condition.index(value)
        condition[index] = new_value
result = ' '.join(condition)
condition = (" ".join(map(str, condition)))
day_time, minutes, temperature = 5, "17", 5
condition = f'в "{day_time:02d}" часов "{minutes}" минут температура воздуха была "+{temperature:02d}" градусов'

print(condition)
# превращаем список в строку
condition = (" ".join(map(str, condition)))

# форматируем строку
day_time, minutes, temperature = 5, "17", 5
condition = f'в "{day_time:02d}" часов "{minutes}" минут температура воздуха была "+{temperature:02d}" градусов'

print(condition)
