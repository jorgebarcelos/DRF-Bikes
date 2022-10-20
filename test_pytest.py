import requests


class TestBikes:
    headers = {"Authorization": "Token 047b9255295a09da37d75081fe1c6ab24d7fcd68"}
    bikes_url = "http://127.0.0.1:8000/api/v2/bikes/"

    def test_get_bikes(self):
        bikes = requests.get(url=self.bikes_url, headers=self.headers)
        assert bikes.status_code == 200

    def test_get_bike(self):
        id = 1
        bike = requests.get(url=f"{self.bikes_url}{id}", headers=self.headers)
        assert bike.status_code == 200

    def test_post_bike(self):
        payload = {"model_name": "Harley Davidson Iron 1200", "engine_power": "1200cc"}
        result = requests.post(url=self.bikes_url, headers=self.headers, data=payload)
        assert result.status_code == 201
        assert result.json()["model_name"] == payload["model_name"]

    def test_put_bike(self):
        id = 1
        updated = {"model_name": "Harley Davidson Iron 883", "engine_power": "883cc"}
        updated_response = requests.put(
            url=f"{self.bikes_url}{id}/", headers=self.headers, data=updated
        )
        assert updated_response.status_code == 200
        assert updated_response.json()["model_name"] == updated["model_name"]

    def test_delete_bike(self):
        id = 5
        response = requests.delete(url=f'{self.bikes_url}{id}/', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0
