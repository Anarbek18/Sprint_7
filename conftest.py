import pytest

import helpers


@pytest.fixture
def courier_payload():
    """Данные нового курьера (без регистрации). После теста курьер удаляется, если был создан."""
    payload = helpers.generate_courier_payload()
    yield payload
    helpers.cleanup_courier(payload["login"], payload["password"])


@pytest.fixture
def registered_courier(courier_payload):
    """Уже зарегистрированный курьер."""
    response = helpers.create_courier(courier_payload)
    assert response.status_code == 201, "Не удалось подготовить курьера для теста"
    return courier_payload
