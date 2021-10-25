"""

Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""


from collections import Counter  # импортируем каунтер


def parce_data(file):  # функция парсинга из файла

    """
    :param file: берем файл логов
    :return: ip с наибольшим количством обрашений и само количество обращений
    """

    result = []  # прописываем переменную нашего конечного результата
    with open(file, 'r', encoding='utf-8') as fn:  # открываем наш файл
        for _ in fn:  # перебираем значения
            string = _.strip()
            rem_ip, _, _, _, _, request_type, requested_resource, *_ = string.split()
            result.append(tuple((rem_ip, request_type[1:], requested_resource)))
        spam_ip = []
        for item in result:  # выводим нашего спамера
            spam_ip.append(item[0])
        hi_scores = Counter(spam_ip)
        max_par = max(hi_scores.values())
        spam_addr = list(hi_scores.keys())[list(hi_scores.values()).index(max_par)]
        spam = f'ip: {spam_addr} количество запросов: {max_par}'
    return spam, result


logs = 'nginx_logs.txt'
spam_ip, logs_list = parce_data(logs)
print(len(logs_list))
print(spam_ip)
