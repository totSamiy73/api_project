from endpoints.base_endpoint import Endpoint
import requests
import allure

class GetMeme(Endpoint):

    @allure.step("Получаем мем по id")
    def get_meme(self, id_meme, token):
        self.response = requests.get(f"{self.BASE_URL}/meme/{id_meme}", headers=token)
        return self.response

