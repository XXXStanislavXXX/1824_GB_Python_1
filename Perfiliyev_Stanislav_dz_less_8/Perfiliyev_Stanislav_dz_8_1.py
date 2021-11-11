"""

Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:

email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?

"""

import re
MAIL_COMPILLER = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9]+)+$')  # компилируем иеил


def mail_parse(email_address):  # задаем функцию
    if MAIL_COMPILLER.match(email_address):  # если попало в нашу компиляцию, то выдать имя пользователя и домен
        keys = ['username', 'domain']
        return dict(zip(keys, email_address.split('@')))
    else:
        raise ValueError(f'ValueError: wrong email: {email_address}')  # если нет, то не верно введен маил


print(mail_parse('aksjd@lksbka.ru'))  # абракадабра, но верно скомпилирована

# print(mail_parse('kansflkngkjlkkas.com'))  # нет собаки

# print(mail_parse('lasv@lnk;a.'))  # нет соотношения домена
