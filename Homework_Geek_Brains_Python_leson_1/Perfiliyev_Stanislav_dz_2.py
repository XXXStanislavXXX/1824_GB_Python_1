"""

Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
списка, сумма цифр которых делится нацело на 7.
c. * Решить задачу под пунктом b, не создавая новый список.

"""

numbers_list = []
total = 0
new_total = 0
for base_element in range(1, 1000, 2):
    numbers_list.append(base_element ** 3)
    element = numbers_list[-1]
    num = element
    sum = 0
    for simbol in str(element):
        sum += int(simbol)
    if sum % 7 == 0:
        total = total + element
print("задание а = " + str(total))
numbers_list[:] = [i + 17 for i in numbers_list]
for new_element in numbers_list:
    new_num = new_element
    new_sum = 0
    for simbol in str(new_element):
        new_sum += int(simbol)
    if new_sum % 7 == 0:
            new_total = new_total + new_element
print("задание б/с = " + str(new_total))
