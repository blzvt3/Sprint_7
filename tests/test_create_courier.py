import requests
import allure
import urls
from data import Data

class TestCreateCourier:
    @allure.title('Проверка создания курьера - заполнены все обязательные поля')
    def test_create_courier(self, delete_courier):
        payload = {"login": Data.login, "password": Data.password, "firstName": Data.firstName}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title('Проверка создания курьера - не указан пароль')
    def test_create_courier_no_password(self):
        payload = {"login": Data.login, "password": "", "firstName": Data.firstName}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
        assert response.status_code == 400 and response.json() == {"code": 400, "message": Data.create_courier_400_error}

    @allure.title('Проверка создания курьера - не указан логин')
    def test_create_courier_no_login(self):
        payload = {"login": "", "password": Data.password, "firstName": Data.firstName}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
        assert response.status_code == 400 and response.json() == {"code": 400, "message": Data.create_courier_400_error}

    @allure.title('Проверка создания курьера - указан существующий логин')
    def test_create_courier_login_exist(self, create_and_delete_courier_login_exist):
        payload = {"login": Data.login_exist, "password": Data.password_exist, "firstName": Data.firstName_exist}
        response = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
        assert response.status_code == 409 and response.json() == {"code": 409, "message": Data.create_courier_409_error}