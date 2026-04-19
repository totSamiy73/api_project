from endpoints.base_endpoint import Endpoint
import requests
import allure


class GetAuthorized(Endpoint):

    @allure.step('Активность токена')
    def get_authorize_token(self, token=None):
        token = self.AUTH_TOKEN["Authorization"] if token is None else token
        self.response = requests.get(f"{self.BASE_URL}/authorize/{token}")
        return self.response

    @allure.step('Проверяем текст ответа активности токена')
    def check_text_get_authorize_token(self):
        text = self.response.text
        assert text.startswith("Token is alive. Username is"), "Текст ответа не содержит Token is alive. Username is"

    @allure.title("Проверка активного токена через POST запрос")
    def get_authorize_invalid_method(self):
        self.response = requests.post(f"{self.BASE_URL}/authorize/{self.AUTH_TOKEN}")
        return self.response
