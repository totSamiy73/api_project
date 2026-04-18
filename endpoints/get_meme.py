from endpoints.base_endpoint import Endpoint
import requests
import allure


class GetMeme(Endpoint):

    @allure.step("Получаем мем по id")
    def get_meme(self, id_meme, token):
        self.response = requests.get(f"{self.BASE_URL}/meme/{id_meme}", headers=token)
        return self.response

    @allure.step("Проверяем, что повторный GET возвращает тот же результат")
    def check_double_get_meme(self, id_meme, token):
        response1 = requests.get(f"{self.BASE_URL}/meme/{id_meme}", headers=token)
        response2 = requests.get(f"{self.BASE_URL}/meme/{id_meme}", headers=token)
        assert response1.status_code == response2.status_code, "Статус коды разные у одинаковых запросов GET"
        assert response1.json() == response2.json(), "Тело у мемов разные при одинаковых запросах GET"

    @allure.step("Получаем мем через POST запрос")
    def get_meme_invalid_method(self, id_meme, token):
        self.response = requests.post(f"{self.BASE_URL}/meme/{id_meme}", headers=token)


