import allure
import pytest

import data
import helpers


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться: код 200 и в теле есть id")
    def test_login_success_returns_id(self, registered_courier):
        response = helpers.login_courier(
            {"login": registered_courier["login"], "password": registered_courier["password"]}
        )

        assert response.status_code == 200
        assert isinstance(response.json().get("id"), int)

    @allure.title("Без поля '{missing_field}' возвращается 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_without_required_field_returns_400(self, registered_courier, missing_field):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        payload.pop(missing_field)

        response = helpers.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == data.MSG_NOT_ENOUGH_LOGIN

    @allure.title("Неверный '{wrong_field}' -> 404 'Учетная запись не найдена'")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_credentials_returns_404(self, registered_courier, wrong_field):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        payload[wrong_field] = helpers.generate_random_string(12)

        response = helpers.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == data.MSG_ACCOUNT_NOT_FOUND

    @allure.title("Несуществующий пользователь -> 404")
    def test_login_nonexistent_user_returns_404(self):
        response = helpers.login_courier(
            {"login": helpers.generate_random_string(12), "password": helpers.generate_random_string(12)}
        )

        assert response.status_code == 404
        assert response.json()["message"] == data.MSG_ACCOUNT_NOT_FOUND
