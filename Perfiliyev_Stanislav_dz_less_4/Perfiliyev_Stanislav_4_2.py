from cbr_parser import extract_data, extract_date  # берем интересующую функцию из парсера


def currency_rates(currency_code: str):
    currency_code = currency_code.upper()
    data = {}
    char_code = extract_data("CharCode")
    cur_value = extract_data("Value")
    zip_result = zip(char_code, cur_value)
    for name, cur_value in zip_result:
        data.setdefault(name, cur_value)
    if currency_code in data:
        new_data = round(float(str(data[currency_code]).replace(",", ".")), 2)
        return new_data, extract_date()
    else:
        return None, extract_date()


val_code = input("введите международный код валюты :")
cur_cost, cur_date = (currency_rates(val_code))
print(cur_cost, cur_date, sep=', ')
