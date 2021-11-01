from cbr_parser import extract_date, currency_rates  # испортируем модули парсера


def ref_cur_rates(argv: str):  # задаем рефактор новой функции
    module, arg = argv  # задаем переменные
    cur_cost, cur_date = currency_rates(arg)  # интерпретация функции
    return cur_cost, cur_date  # выводим итог


if __name__ == '__main__':  # проверка на запуск по аналогу с методичкой
    import sys
    if len(sys.argv) > 1:
        cur_cost, cur_date = ref_cur_rates(sys.argv)
    else:
        cur_cost = None
        cur_date = extract_date()
    exit(print(cur_cost, cur_date, sep=', '))
