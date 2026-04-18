import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetAllMeme(Endpoint):

    @allure.step("Получаем все мемы")
    def get_all_meme(self, head):
        self.response = requests.get(f"{self.BASE_URL}/meme", headers=head)
        return self.response

    @allure.step("Структура ответа всех мемов")
    def check_body_get_all_meme(self):
        js = self.response.json()
        assert isinstance(js, dict), "ответ на запрос всех мемов содержит не dict"
        assert 'data' in js, "отсутствует поле data в ответе при запросе всех мемов"
        assert isinstance(js['data'], list), "поле data в ответе при запросе всех мемов содержит не list"



    @allure.step("Неверный метод запроса всех мемов POST")
    def get_all_meme_invalid_method(self):
        self.response = requests.post(f"{self.BASE_URL}/meme", headers=self.AUTH_TOKEN)
        return self.response
