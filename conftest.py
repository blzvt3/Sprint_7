import requests
import urls
import pytest
from data import Data

@pytest.fixture
def create_and_delete_courier_login_exist():
    payload = {"login": Data.login_exist, "password": Data.password_exist, "firstName": Data.firstName_exist}
    response_create = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
    assert response_create.status_code == 201 and response_create.json() == {"ok": True}

    yield

    payload = {"login": Data.login_exist, "password": Data.password_exist}
    response_login = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
    assert response_login.status_code == 200 and "id" in response_login.json()
    courier_id = response_login.json().get("id")

    response_delete = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT.format(courier_id))
    assert response_delete.status_code == 200 and response_delete.json() == {"ok": True}

@pytest.fixture
def delete_courier():
    yield

    payload = {"login": Data.login, "password": Data.password}
    response_login = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
    assert response_login.status_code == 200 and "id" in response_login.json()
    courier_id = response_login.json().get("id")

    response_delete = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT.format(courier_id))
    assert response_delete.status_code == 200 and response_delete.json() == {"ok": True}