from endpoints.base_endpoint import Endpoint
import allure
import requests

class PutMeme(Endpoint):

    @allure.step("Обновляем мем")
    def put_meme(self, id_meme, body, token):
        self.response = requests.put(f"{self.BASE_URL}/meme/{id_meme}", json=body, headers=token)
        return self.response

    @allure.step("Обновление мема через POST запрос")
    def put_meme_invalid_method(self, id_meme, body, token):
        self.response = requests.post(f"{self.BASE_URL}/meme/{id_meme}", json=body, headers=token)
        return self.response

    @allure.step("Проверяем, что повторный PUT возвращает тот же результат")
    def check_double_put_meme(self, id_meme, body, token):
        response1 = requests.put(f"{self.BASE_URL}/meme/{id_meme}", json=body, headers=token)
        response2 = requests.put(f"{self.BASE_URL}/meme/{id_meme}", json=body, headers=token)
        assert response1.status_code == response2.status_code, "Статус коды разные у одинаковых запросов PUT"
        assert response1.json() == response2.json(), "Тело у мемов разные при одинаковых запросах PUT"






