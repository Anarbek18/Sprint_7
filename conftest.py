@pytest.fixture
def courier_payload():
    """Данные нового курьера (без регистрации)."""
    return helpers.generate_courier_payload()


@pytest.fixture
def courier_cleanup(courier_payload):
    """Удаляет курьера после теста (после ассертов), если он был создан."""
    yield
    helpers.cleanup_courier(courier_payload["login"], courier_payload["password"])


@pytest.fixture
def registered_courier(courier_payload, courier_cleanup):
    """Уже зарегистрированный курьер (удаляется после теста через courier_cleanup)."""
    response = helpers.create_courier(courier_payload)
    assert response.status_code == 201, "Не удалось подготовить курьера для теста"
    return courier_payload