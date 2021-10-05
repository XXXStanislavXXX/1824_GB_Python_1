def list_mask(list_name):
    result = ''
    for price in list_name:
        result += f'{int(price):d} руб {int(round((price - int(price)) * 100)):02d} коп, '
    return result
prices = [844.32, 1523.54, 467.17, 235.85, 614.72, 1436.4, 651.85, 1625.0, 321.81]
print(list_mask(prices), 'ID списка: ', id(prices))
prices.sort()
print(list_mask(prices), 'ID списка: ', id(prices))
prices_reversed = list(reversed(prices))
print(list_mask(prices_reversed), 'ID списка: ', id(prices_reversed))
top_5 = list(reversed(prices_reversed[:5]))
print(list_mask(top_5), 'ID списка: ', id(top_5))