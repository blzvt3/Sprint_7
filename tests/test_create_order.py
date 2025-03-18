import requests
import allure
import urls
import pytest

class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize(
        ("firstName", "lastName", "address", "metroStation", "phone", "rentTime", "deliveryDate", "comment", "color"),
        [("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["BLACK"]),
         ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["GREY"]),
         ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["BLACK", "GREY"]),
         ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", [])
         ])
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