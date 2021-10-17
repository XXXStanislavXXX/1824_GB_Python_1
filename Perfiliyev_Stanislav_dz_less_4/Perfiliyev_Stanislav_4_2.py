from cbr_parser import extract_data  # берем интересующую функцию из парсера
from cbr_parser import send_request


print(send_request())


def currency_rates(currency_code: str):
    currency_code = currency_code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    value = extract_data("Value")
    zip_result = zip(ch_code, value)
    for name, value in zip_result:
        data.setdefault(name, value)
    if currency_code in data:
        new_data = str(data[currency_code]).replace(",", ".")
        return round(float(new_data), 2)
    else:
        return None


print(currency_rates(input("введите код валюты :")))
