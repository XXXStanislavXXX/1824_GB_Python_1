"""

*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
 реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат
 тоже должен быть с заглавной. Например:

num_translate_adv("One")
"Один"
num_translate_adv("two") -> Ошибка в условии? вроде как должно было быть тоже с большой?
"два"

"""

def num_translate_adv(number: str) -> str:

    """функция перевода, введите пожалуйста цифру в виде str на английском """

    translation_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
    }
    if number[0].isupper():
        number = number.lower()
        if number in translation_dict:
            print(number.capitalize(), "на русском: ", (translation_dict[number]).capitalize())
    else:
        number = number.lower()
        if number in translation_dict:
            print(number, "на русском: ", (translation_dict[number]))


num_translate_adv(input('введите цифру на английском: '))
