import requests
import allure
import urls

class TestGetOrders:
    @allure.title('Проверка получения списка заказов')
    def test_get_orders(self):
        response = requests.get(urls.BASE_URL + urls.ORDER_ENDPOINT)
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)