"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:

get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


"""

import random # вводим переменную рандом


def get_jokes(jokes_count: int, no_retry=False) -> None:  # задаём функцию

    """

    Составляет шутку из значений списка: nouns, adverbs, adjectives
    :param jokes_count: Количество шуток
    :param no_retry: True - без повторов/False - с повторами (значение по умолчанию)

    """
    base_joke = []
    joke_quantity = []
    base_joke_stat = []
    quantity = jokes_count
    copies = 0
    result = []
    if no_retry is True:  # условие без повторов
        quantity = 1
        copies = len(nouns)
    if jokes_count > len(nouns) and no_retry is True:  # если без повторов но слишком много шуток надо
        print('Количество значений в списке недостаточно, чтобы вывсести без повторов '
              'Добавте пожалуйста значений в списки '
              )
        quantity = 1
        copies = len(nouns)
    for step in range(quantity):
        base_joke.extend(random.sample(nouns, copies))
        joke_quantity.extend(random.sample(adverbs, copies))
        base_joke_stat.extend(random.sample(adjectives, copies))
    for thing, time, about in zip(base_joke, joke_quantity, base_joke_stat):
        result.append(f'{thing} {time} {about}')
    print(result[0:jokes_count])


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(4, True)

get_jokes(10, True)
