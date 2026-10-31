import allure
import pytest

import data
import helpers


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать: код 201 и тело {'ok': true}")
    def test_create_courier_success(self, courier_payload, courier_cleanup):
        response = helpers.create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров: код 409")
    def test_create_duplicate_courier_returns_409(self, registered_courier):
        response = helpers.create_courier(registered_courier)

        assert response.status_code == 409
        assert response.json()["message"] == data.MSG_LOGIN_TAKEN

    @allure.title("Нельзя создать курьера с уже существующим логином")
    def test_create_courier_with_existing_login_returns_409(self, registered_courier):
        payload = helpers.generate_courier_payload()
        payload["login"] = registered_courier["login"]

        response = helpers.create_courier(payload)

        assert response.status_code == 409
        assert response.json()["message"] == data.MSG_LOGIN_TAKEN

    @allure.title("Без обязательного поля '{missing_field}' возвращается 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_400(self, courier_payload, missing_field):
        payload = {k: v for k, v in courier_payload.items() if k != missing_field}

        response = helpers.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == data.MSG_NOT_ENOUGH_CREATE
