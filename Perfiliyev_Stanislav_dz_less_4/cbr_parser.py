import datetime
from datetime import date
import requests
import re
import sys
import typing
from pyquery import PyQuery as p_q
from lxml import etree
from pprint import pprint


URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


def extract_data(tag: str) -> typing.List:
    """Извлекает данные из соответствующего тега и возвращает список string значений"""
    res = send_request()
    main_root = p_q(etree.fromstring(res.content))
    curs_val = main_root.pop()
    return curs_val.xpath(f'//Valute/{tag}/text()')


def extract_date() -> datetime.date:
    """Извлекает текущую дату из данных"""
    res = send_request()
    data = re.findall(r'<ValCurs Date="(.*)" name="Foreign Currency Market"', str(res.content))
    data_parts = data[0].split(".")
    result = [int(item) for item in data_parts]
    day, month, year = result[0], result[1], result[2]
    cur_date = date(day=day, month=month, year=year)
    return cur_date


def currency_rates(code: str):
    code = code.upper()
    data = {}
    ch_code = extract_data("CharCode")
    val = extract_data("Value")
    zip_res = zip(ch_code, val)
    for name, value in zip_res:
        data.setdefault(name, value)
    if code in data:
        new_data = round(float(str(data[code]).replace(",", ".")), 2)
        return new_data, extract_date()
    else:
        return None, extract_date()

if __name__ == '__main__':
    # пример использования
    name_valutes = extract_data('Name')
    pprint(name_valutes)
