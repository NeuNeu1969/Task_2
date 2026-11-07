import pytest

from api.user_api import UserApi
from api.order_api import OrderApi
from helpers import generate_user_data


@pytest.fixture
def user_data():
    # Данные нового пользователя, после теста удаление
    data = generate_user_data()
    tokens = []
    yield data, tokens
    for token in tokens:
        UserApi().delete_user(token)


@pytest.fixture
def registered_user(user_data):
    # Регистрация пользователя, передача данных и токена в тест
    data, tokens = user_data
    response = UserApi().register_user(data)
    token = response.json()["accessToken"]
    tokens.append(token)
    return {"data": data, "token": token}


@pytest.fixture
def ingredients():
    # Хеши двух первых ингредиентов
    response = OrderApi().get_ingredients()
    return [item["_id"] for item in response.json()["data"][:2]]
