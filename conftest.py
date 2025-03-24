import requests
import urls
import pytest
from data import Data

@pytest.fixture
def create_and_delete_courier_login_exist():
    login, password, first_name = Data.fake_data()
    payload = {"login": login, "password": password, "firstName": first_name}
    response_create = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
    if response_create.status_code != 201 or response_create.json() != {"ok": True}:
        pytest.fail(f"Ошибка при создании курьера: {response_create.status_code}, {response_create.text}")

    yield login, password, first_name

    payload = {"login": login, "password": password}
    response_login = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
    if response_login.status_code != 200 or "id" not in response_login.json():
        pytest.fail(f"Ошибка при авторизации курьера: {response_login.status_code}, {response_login.text}")

    courier_id = response_login.json().get("id")
    response_delete = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT.format(courier_id))
    if response_delete.status_code != 200 or response_delete.json() != {"ok": True}:
        pytest.fail(f"Ошибка при удалении курьера: {response_delete.status_code}, {response_delete.text}")

@pytest.fixture
def delete_courier():
    login, password, first_name = Data.fake_data()
    yield login, password, first_name

    payload = {"login": login, "password": password}
    response_login = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
    if response_login.status_code != 200 or "id" not in response_login.json():
        pytest.fail(f"Ошибка при авторизации курьера: {response_login.status_code}, {response_login.text}")

    courier_id = response_login.json().get("id")
    response_delete = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT.format(courier_id))
    if response_delete.status_code != 200 or response_delete.json() != {"ok": True}:
        pytest.fail(f"Ошибка при удалении курьера: {response_delete.status_code}, {response_delete.text}")