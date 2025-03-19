import requests
import allure
import urls
import pytest
from data import Data

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize(("firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "comment", "color"), Data.order_data)
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {
    "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metroStation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": color
}
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload)
        assert response.status_code == 201
        response_json = response.json()
        assert "track" in response_json
        assert isinstance(response_json["track"], int)