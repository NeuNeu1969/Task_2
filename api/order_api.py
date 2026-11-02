import allure

from api.base_api import BaseApi
from urls import INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT


class OrderApi(BaseApi):

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return self.send_request("GET", INGREDIENTS_ENDPOINT)

    @allure.step("Создать заказ")
    def create_order(self, ingredients, token=None):
        return self.send_request("POST", ORDERS_ENDPOINT, json_body={"ingredients": ingredients}, token=token)

    @allure.step("Получить заказы пользователя")
    def get_user_orders(self, token=None):
        return self.send_request("GET", ORDERS_ENDPOINT, token=token)
