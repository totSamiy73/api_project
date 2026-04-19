from endpoints.base_endpoint import Endpoint
import allure
import requests


class PostAuthorize(Endpoint):

    @allure.step("Авторизация пользователя")
    def post_authorize(self, body):
        self.response = requests.post(f"{self.BASE_URL}/authorize", json=body)
        return self.response

    @allure.step("Структура ответа авторизации пользователя")
    def check_body_post_authorize(self, user):
        js = self.response.json()
        assert isinstance(js, dict), "В ответе не dict"
        required_fields = ["token", "user"]
        for field in required_fields:
            assert field in js, f"У объекта отсутствует обязательное поле {field} при регистрации"
        assert isinstance(js['token'], str), f"Поле token не str\n{js}"
        assert len(js['token']) == 15, "Длина токена больше или меньше 15"
        assert isinstance(js['user'], str), f"Поле user не str\n{js}"
        assert js['user'] == user['name'], f"Поле user содержит не те данные что отправили\n{js}"

    @allure.title("Авторизация пользователя через PUT запрос")
    def post_authorize_invalid_method(self, body):
        self.response = requests.put(f"{self.BASE_URL}/authorize", json=body)
        return self.response
