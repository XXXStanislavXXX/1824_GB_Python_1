"""

Вывод продаж через cmd

"""

def sales_output(argv):

    """
    :param argv: принимает аргументом порядковый номер продажи, типа " " - для вывода всех продаж 1 3 - для вывода
    продаж от 1 до 3, 2 - для вывода конкретной продажи с конкретным id
    :return: значение из bakery.csv, соответствующее порядковому номеру
    """

    program, *arg = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if (len(sys.argv)-1) == 0:
            line = f.readlines()
            for i in range(len(line)):
                print(f'{str(i + 1)} : {line[i].strip()}')
        elif (len(sys.argv)-1) == 1:
            line = f.readlines()
            begin = int(''.join(arg[0]))
            for i in range(begin - 1, len(line)):
                print(f'{str(i + 1)} : {line[i].strip()}')
        elif (len(sys.argv)-1) == 2:
            line = f.readlines()
            begin = int(''.join(arg[0]))
            end = int(''.join(arg[1]))
            if end <= len(line):
                for i in range(begin - 1, end):
                    print(f'{str(i + 1)} : {line[i].strip()}')
            else:
                for i in range(begin - 1, len(line)):
                    print(f'{str(i + 1)} : {line[i].strip()}')



if __name__ == '__main__':
    import sys
    exit(sales_output(sys.argv))
