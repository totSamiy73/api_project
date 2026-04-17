import allure
correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
               "tags": ["cat", "bu"],
               "text": "Бу! испугался?!",
               "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}

class Endpoint:
    BASE_URL = "http://memesapi.course.qa-practice.com"
    AUTH_TOKEN = {"Authorization": "IGhQfTB49JgOFxT"}
    response = None

    @allure.step("Статус код ответа")
    def check_response_status_code(self, status_code):
        with allure.step(f"Проверяем статус код {status_code}"):
            actual_sc = self.response.status_code
            assert actual_sc == status_code, f"неверный статус код, ожидали {status_code}, получили {actual_sc}"

    @allure.step("Время ответа при запросе")
    def check_time_response(self):
        with allure.step(f"Проверяем время ответа метода {self.response.request.method}"):
            time = self.response.elapsed.total_seconds()
            assert time < 1, "время ответа более 1 сек"

    @allure.step("Структура мема")
    def check_body_meme(self):
        with allure.step(f"Проверяем структуру ответа"):
            required_fields = ["id", "info", "tags", "text", "updated_by", "url"]
            js = self.response.json()
            assert isinstance(js, dict), "В ответе не dict"
            for field in required_fields:
                assert field in js, f"У объекта id={js.get('id')} отсутствует обязательное поле {field}"
            assert isinstance(js['id'], int), "Поле id не int"

            assert isinstance(js['info'], dict), "Поле info не dict"
            assert js['info'] == correct_body['info'], "Поле info содержит не те данные что отправили"

            assert isinstance(js['tags'], list), "Поле tags не list"
            assert js['tags'] == correct_body['tags'], "Поле tags содержит не те данные что отправили"

            assert isinstance(js['text'], str), "Поле text не str"
            assert js['text'] == correct_body['text'], "Поле text содержит не те данные что отправили"

            assert isinstance(js['updated_by'], str), "Поле updated_by не str"
            assert js['updated_by'] == "tot", "Поле text содержит не те данные что отправили"

            assert isinstance(js['url'], str), "Поле url не str"
            assert js['url'] == correct_body['url'], "Поле url содержит не те данные что отправили"
