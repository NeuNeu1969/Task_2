import allure

from api.base_api import BaseApi
from urls import REGISTER_ENDPOINT, LOGIN_ENDPOINT, USER_ENDPOINT


class UserApi(BaseApi):

    @allure.step("Создать пользователя")
    def register_user(self, payload):
        return self.send_request("POST", REGISTER_ENDPOINT, json_body=payload)

    @allure.step("Авторизовать пользователя")
    def login_user(self, payload):
        return self.send_request("POST", LOGIN_ENDPOINT, json_body=payload)

    @allure.step("Изменить данные пользователя")
    def update_user(self, payload, token=None):
        return self.send_request("PATCH", USER_ENDPOINT, json_body=payload, token=token)

    @allure.step("Удалить пользователя")
    def delete_user(self, token):
        return self.send_request("DELETE", USER_ENDPOINT, token=token)
