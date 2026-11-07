import allure
import pytest

from api.user_api import UserApi
from data import (
    STATUS_OK,
    STATUS_FORBIDDEN,
    USER_EXISTS_MESSAGE,
    REQUIRED_FIELDS_MESSAGE,
    USER_REQUIRED_FIELDS,
)


@allure.feature("Пользователь")
@allure.story("Создание пользователя")
class TestCreateUser:

    @allure.title("Уникального пользователя можно создать")
    def test_create_unique_user_success(self, user_data):
        data, tokens = user_data
        # Регистрация нового пользователя
        response = UserApi().register_user(data)
        tokens.append(response.json()["accessToken"])

        # Проверка кода и данных пользователя в ответе
        assert response.status_code == STATUS_OK
        assert response.json()["user"] == {"email": data["email"], "name": data["name"]}

    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    def test_create_existing_user_returns_error(self, registered_user):
        # Повторная регистрация с теми же данными
        response = UserApi().register_user(registered_user["data"])

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_FORBIDDEN
        assert response.json()["message"] == USER_EXISTS_MESSAGE

    @allure.title("Без обязательного поля пользователя создать нельзя")
    @pytest.mark.parametrize("missing_field", USER_REQUIRED_FIELDS)
    def test_create_user_without_required_field_returns_error(self, user_data, missing_field):
        data, tokens = user_data
        # Удаление обязательного поля
        payload = data.copy()
        payload.pop(missing_field)
        response = UserApi().register_user(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_FORBIDDEN
        assert response.json()["message"] == REQUIRED_FIELDS_MESSAGE
