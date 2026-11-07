import allure
import pytest

from api.user_api import UserApi
from data import STATUS_OK, STATUS_UNAUTHORIZED, UNAUTHORISED_MESSAGE, USER_UPDATE_FIELDS
from helpers import generate_user_data


@allure.feature("Пользователь")
@allure.story("Изменение данных пользователя")
class TestUpdateUser:

    @allure.title("Авторизованный пользователь может изменить любое поле")
    @pytest.mark.parametrize("field", USER_UPDATE_FIELDS)
    def test_update_user_with_auth_success(self, registered_user, field):
        # Новое значение поля
        new_value = generate_user_data()[field]
        response = UserApi().update_user({field: new_value}, registered_user["token"])

        # Проверка кода и признака успеха
        assert response.status_code == STATUS_OK
        assert response.json()["success"] is True

    @allure.title("Без авторизации изменить данные нельзя")
    @pytest.mark.parametrize("field", USER_UPDATE_FIELDS)
    def test_update_user_without_auth_returns_error(self, field):
        # Запрос без токена
        new_value = generate_user_data()[field]
        response = UserApi().update_user({field: new_value})

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_UNAUTHORIZED
        assert response.json()["message"] == UNAUTHORISED_MESSAGE
