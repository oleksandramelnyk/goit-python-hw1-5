"""
Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет.
Реализуйте функцию lookup_key для поиска всех ключей по значению в словаре.
Первым параметром в функцию мы передаем словарь, а вторым — значение, которое хотим найти.
Таким образом результат может быть как список ключей, так и пустой список, если мы ничего не найдем.
"""


def lookup_key(data, value):
    keys_found = []

    for k, v in data.items():
        if v == value:
            keys_found.append(k)

    return keys_found
