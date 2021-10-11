"""

Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:

thesaurus("Иван", "Мария", "Петр", "Илья")

{
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}


Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?

"""


def thesaurus(*args: str) -> dict:

    """Словарь по первой букве имени"""

    names_dict = {}
    for name in args:
        if name[0] in names_dict:
            old_name = names_dict[name[0]]
            names_dict[name[0]] = [*old_name, name]
        else:
            names_dict.setdefault(name[0], [name])
    return names_dict


name_set = ("Иван", "Мария", "Петр", "Илья", "Михаил", "Полина", "Анатолий", "Эллина", "Ангелина")
final_dict = thesaurus(*name_set)
keys_set = list(final_dict.keys())
keys_set.sort()
for x in keys_set:
    print(f'"{x}": {final_dict[x]}')
