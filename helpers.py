import random
import string


def generate_random_string(length):
    # Случайная строка из латинских букв
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_user_data():
    # Почта, пароль и имя пользователя
    return {
        "email": generate_random_string(10) + "@yandex.ru",
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }
