BASE_URL = "https://qa-scooter.education-services.ru"

COURIER_URL = f"{BASE_URL}/api/v1/courier"
LOGIN_URL = f"{BASE_URL}/api/v1/courier/login"
ORDERS_URL = f"{BASE_URL}/api/v1/orders"

# Тексты ошибок из документации API
MSG_LOGIN_TAKEN = "Этот логин уже используется. Попробуйте другой."
MSG_NOT_ENOUGH_CREATE = "Недостаточно данных для создания учетной записи"
MSG_NOT_ENOUGH_LOGIN = "Недостаточно данных для входа"
MSG_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-12-06",
    "comment": "Saske, come back to Konoha",
}
