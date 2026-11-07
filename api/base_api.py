import allure
import requests

from constants import REQUEST_TIMEOUT
from urls import BASE_URL


class BaseApi:

    @allure.step("Отправить запрос к API")
    def send_request(self, method, path, json_body=None, token=None):
        # Токен передаётся в заголовке Authorization
        headers = {"Authorization": token} if token else None
        return requests.request(
            method,
            BASE_URL + path,
            json=json_body,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
