from cbr_parser import extract_data, extract_date  # берем интересующую функцию из парсера


def currency_rates(currency_code: str):  # задаем саму функцию по отображению валюты по ее ниже введенному коду
    currency_code = currency_code.upper()  # заранее правим регистр
    data = {}  # задаем словарик, который позже заполним значениями
    char_code = extract_data("CharCode")  # задаем переменные, которые нам поставил наш парсер
    cur_value = extract_data("Value")  # задаем переменные, которые нам поставил наш парсер
    zip_result = zip(char_code, cur_value)  # запаковываем обе переменные
    for name, cur_value in zip_result:
        data.setdefault(name, cur_value)  # выводим курс
    if currency_code in data:  # условие, что код написан верно
        new_data = round(float(str(data[currency_code]).replace(",", ".")), 2)  # задаем формат вывода
        return new_data, extract_date()  # сам вывод + дата
    else:
        return None, extract_date()  # если написан не верный код + дата


val_code = input("введите код валюты :")
cur_cost, cur_date = (currency_rates(val_code))
print(cur_cost, cur_date, sep=', ')
