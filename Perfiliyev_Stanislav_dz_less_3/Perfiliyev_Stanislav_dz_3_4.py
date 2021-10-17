"""

*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?

"""


def thesaurus_adv(*args: str) -> dict:
    """
    Создает словарь из имени и фамилии - первый ключ по фамилии и вложенный по имени

    """
    names_dict = {}
    for name in args:
        if (name.split()[-1])[0] in names_dict:
            if name[0] in names_dict[(name.split()[-1])[0]]:
                old_name = names_dict[(name.split()[-1])[0]][name[0]]
                names_dict[(name.split()[-1])[0]][name[0]] = [*old_name, name]
            else:
                (names_dict[(name.split()[-1])[0]]).setdefault(name[0], [name])
        else:
            names_dict.setdefault((name.split()[-1])[0], {name[0]: [name]})
    return names_dict


names_set = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
result_dict = thesaurus_adv(*names_set)
keys_set = list(result_dict.keys())
keys_set.sort()
for i in keys_set:
    print(f'"{i}": {result_dict[i]}')
