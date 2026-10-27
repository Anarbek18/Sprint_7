import allure

import helpers


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В теле ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = helpers.get_orders()

        assert response.status_code == 200
        orders = response.json()["orders"]
        assert isinstance(orders, list)
        assert len(orders) > 0
