import random
import string

import allure
import requests

import data


def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }


@allure.step("Создать курьера")
def create_courier(payload):
    return requests.post(data.COURIER_URL, json=payload, timeout=15)


@allure.step("Авторизовать курьера")
def login_courier(payload):
    return requests.post(data.LOGIN_URL, json=payload, timeout=15)


@allure.step("Удалить курьера id={courier_id}")
def delete_courier(courier_id):
    return requests.delete(f"{data.COURIER_URL}/{courier_id}", timeout=15)


@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(data.ORDERS_URL, json=payload, timeout=15)


@allure.step("Получить список заказов")
def get_orders():
    return requests.get(data.ORDERS_URL, timeout=15)


def cleanup_courier(login, password):
    """Удаляет курьера, если он существует (логинимся и удаляем по id)."""
    resp = requests.post(data.LOGIN_URL, json={"login": login, "password": password}, timeout=15)
    if resp.status_code == 200:
        delete_courier(resp.json()["id"])
