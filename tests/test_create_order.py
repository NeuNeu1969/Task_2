import allure

from api.order_api import OrderApi
from data import (
    STATUS_OK,
    STATUS_BAD_REQUEST,
    STATUS_SERVER_ERROR,
    NO_INGREDIENTS_MESSAGE,
    INVALID_INGREDIENT_HASH,
)


@allure.feature("Заказ")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Авторизованный пользователь может создать заказ")
    def test_create_order_with_auth_success(self, registered_user, ingredients):
        # Заказ с токеном пользователя
        response = OrderApi().create_order(ingredients, registered_user["token"])

        # Проверка кода и номера заказа
        assert response.status_code == STATUS_OK
        assert "number" in response.json()["order"]

    @allure.title("Заказ без авторизации создаётся")
    def test_create_order_without_auth_success(self, ingredients):
        # Заказ без токена
        response = OrderApi().create_order(ingredients)

        # Проверка кода и номера заказа
        assert response.status_code == STATUS_OK
        assert "number" in response.json()["order"]

    @allure.title("Заказ с ингредиентами создаётся, в ответе есть ингредиенты")
    def test_create_order_with_ingredients_success(self, registered_user, ingredients):
        response = OrderApi().create_order(ingredients, registered_user["token"])

        # Проверка кода и хешей ингредиентов в заказе
        assert response.status_code == STATUS_OK
        assert [item["_id"] for item in response.json()["order"]["ingredients"]] == ingredients

    @allure.title("Без ингредиентов заказ не создаётся")
    def test_create_order_without_ingredients_returns_error(self, registered_user):
        # Заказ с пустым списком ингредиентов
        response = OrderApi().create_order([], registered_user["token"])

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_BAD_REQUEST
        assert response.json()["message"] == NO_INGREDIENTS_MESSAGE

    @allure.title("С неверным хешем ингредиента заказ не создаётся")
    def test_create_order_with_invalid_hash_returns_error(self, registered_user):
        # Заказ с невалидным хешем
        response = OrderApi().create_order([INVALID_INGREDIENT_HASH], registered_user["token"])

        # Проверка кода и текста страницы ошибки
        assert response.status_code == STATUS_SERVER_ERROR
        assert "Internal Server Error" in response.text
