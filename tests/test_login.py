import requests
import allure
import urls

class TestLogin:
    @allure.title('Проверка авторизации - заполнены все обязательные поля')
    def test_login(self):
        payload = {"login": "Art88", "password": "qwe123"}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 200 and response.json() == {"id": 485958}

    @allure.title('Проверка авторизации - неправильно указан пароль')
    def test_login_wrong_password(self):
        payload = {"login": "Art88", "password": "555444"}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 404 and response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title('Проверка авторизации - не указан пароль')
    def test_login_no_password(self):
        payload = {"login": "Art88", "password": ""}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 400 and response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

    @allure.title('Проверка авторизации - не указан логин')
    def test_login_no_login(self):
        payload = {"login": "", "password": "qwe123"}
        response = requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=payload)
        assert response.status_code == 400 and response.json() == {"code": 400, "message": "Недостаточно данных для входа"}