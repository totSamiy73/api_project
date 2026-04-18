from endpoints.base_endpoint import Endpoint
import requests
import allure


class PostMem(Endpoint):

    @allure.step("Создаем мем")
    def create_new_mem(self, body, token):
        self.response = requests.post(f"{self.BASE_URL}/meme", json=body, headers=token)
        return self.response


    @allure.step("Cоздание мема через PUT запрос")
    def post_meme_invalid_method(self, body, token):
        self.response = requests.put(f"{self.BASE_URL}/meme", json=body, headers=token)
        return self.response
