import allure
import pytest

import data
import helpers


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом {color}: код 201 и track в теле")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            [],
        ],
        ids=["black", "grey", "both", "no_color"],
    )
    def test_create_order_with_color(self, color):
        payload = {**data.ORDER_BODY, "color": color}

        response = helpers.create_order(payload)

        assert response.status_code == 201
        assert isinstance(response.json().get("track"), int)

    @allure.title("Создание заказа без поля color вообще")
    def test_create_order_without_color_field(self):
        response = helpers.create_order(data.ORDER_BODY)

        assert response.status_code == 201
        assert "track" in response.json()
