import allure

from api.user_api import UserApi
from data import STATUS_OK, STATUS_UNAUTHORIZED, INCORRECT_LOGIN_MESSAGE
from helpers import generate_random_string


@allure.feature("Пользователь")
@allure.story("Логин пользователя")
class TestLoginUser:

    @allure.title("Существующий пользователь может авторизоваться")
    def test_login_existing_user_success(self, registered_user):
        # Авторизация с почтой и паролем зарегистрированного пользователя
        data = registered_user["data"]
        response = UserApi().login_user({"email": data["email"], "password": data["password"]})

        # Проверка кода и токена в ответе
        assert response.status_code == STATUS_OK
        assert response.json()["accessToken"].startswith("Bearer ")

    @allure.title("С неверным логином и паролем авторизоваться нельзя")
    def test_login_with_wrong_email_and_password_returns_error(self):
        # Незарегистрированные почта и пароль
        payload = {"email": generate_random_string(10) + "@yandex.ru", "password": generate_random_string(10)}
        response = UserApi().login_user(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_UNAUTHORIZED
        assert response.json()["message"] == INCORRECT_LOGIN_MESSAGE
