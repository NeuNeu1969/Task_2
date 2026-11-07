import allure

from api.order_api import OrderApi
from data import STATUS_OK, STATUS_UNAUTHORIZED, UNAUTHORISED_MESSAGE


@allure.feature("Заказ")
@allure.story("Заказы пользователя")
class TestGetUserOrders:

    @allure.title("Авторизованный пользователь получает свои заказы")
    def test_get_orders_with_auth_returns_user_orders(self, registered_user, ingredients):
        # Создание заказа и запрос заказов пользователя
        order_api = OrderApi()
        order_number = order_api.create_order(ingredients, registered_user["token"]).json()["order"]["number"]
        response = order_api.get_user_orders(registered_user["token"])

        # Проверка кода и созданного заказа в списке
        assert response.status_code == STATUS_OK
        assert response.json()["orders"][0]["number"] == order_number

    @allure.title("Неавторизованный пользователь не получает заказы")
    def test_get_orders_without_auth_returns_error(self):
        # Запрос без токена
        response = OrderApi().get_user_orders()

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_UNAUTHORIZED
        assert response.json()["message"] == UNAUTHORISED_MESSAGE
