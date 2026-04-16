from endpoints.base_endpoint import Endpoint
import requests
import allure

correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
               "tags": ["cat", "bu"],
               "text": "Бу! испугался?!",
               "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}


class PostMem(Endpoint):

    @allure.step("Создаем мем")
    def create_new_mem(self, body, token):
        self.response = requests.post(f"{self.BASE_URL}/meme", json=body, headers=token)
        return self.response


    @allure.step("Структура ответа созданного мема")
    def check_body_post_meme(self):
        required_fields = ["id", "info", "tags", "text", "updated_by", "url"]
        js = self.response.json()
        assert isinstance(js, dict), "у созданного мема в ответе не dict"
        for field in required_fields:
            assert field in js, f"У объекта id={js.get('id')} отсутствует обязательное поле {field}"
        assert isinstance(js['id'], int), "у созданного мема поле id не int"

        assert isinstance(js['info'], dict), "у созданного мема поле info не dict"
        assert js['info'] == correct_body['info'], "у созданного мема поле info содержит не те данные что отправили"

        assert isinstance(js['tags'], list), "у созданного мема поле tags не list"
        assert js['tags'] == correct_body['tags'], "у созданного мема поле tags содержит не те данные что отправили"

        assert isinstance(js['text'], str), "у созданного мема поле text не str"
        assert js['text'] == correct_body['text'], "у созданного мема поле text содержит не те данные что отправили"

        assert isinstance(js['updated_by'], str), "у созданного мема поле updated_by не str"
        assert js['updated_by'] == "tot", "у созданного мема поле text содержит не те данные что отправили"

        assert isinstance(js['url'], str), "у созданного мема поле url не str"
        assert js['url'] == correct_body['url'], "у созданного мема поле url содержит не те данные что отправили"

    @allure.step("Дополнительное поле игнорируется при создании мема")
    def check_post_meme_no_additional_field(self):
        js = self.response.json()
        assert "TEST" not in js, "При создании мема появилось дополнительное поле"

    @allure.step("Cоздание мема через PUT запрос")
    def check_post_meme_invalid_method(self, body, token):
        self.response = requests.put(f"{self.BASE_URL}/meme", json=body, headers=token)
        return self.response





