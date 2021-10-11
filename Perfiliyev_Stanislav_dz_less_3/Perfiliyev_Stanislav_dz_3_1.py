"""

Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

"""

def num_translate(number: str) -> str:

    """функция перевода, введите пожалуйста цифру в виде str на английском """

    translation_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    number = number.lower()
    if number in translation_dict:
        return translation_dict[number]
    else:
        return None
        print('нет такой цифры!')


number_in = input('введите цифру: ')
print(number_in, "на русском:", (num_translate(number_in)))
