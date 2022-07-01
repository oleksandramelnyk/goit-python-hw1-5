"""
Задача: надежность пароля
Второй этап. Необходимо написать функцию is_valid_password,
которая будет проверять полученный параметр — пароль на надежность.

Критерии надежного пароля:

Длина строки пароля восемь символов.
Содержит хотя бы одну букву в верхнем регистре.
Содержит хотя бы одну букву в нижнем регистре.
Содержит хотя бы одну цифру.
Функция is_valid_password должна вернуть True, если переданный в качестве параметра
пароль отвечает требованиям надежности. В противном случае вернуть False.
"""


def is_valid_password(password):

    if len(password) != 8:
        return False
    if password == password.lower() or password == password.upper():
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
