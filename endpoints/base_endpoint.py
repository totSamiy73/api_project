import allure
import requests
import time
from colorama import Fore, init
from data_for_tests import main_user

init(autoreset=True)


class Endpoint:
    BASE_URL = "http://memesapi.course.qa-practice.com"
    AUTH_TOKEN = {"Authorization": "IGhQfTB49JgOFxT"}
    LAST_TOKEN_CHECK = 0
    response = None

    def __init__(self):
        # оптимизируем проверку токена, осознано оставляю захардкоженный токен,
        # не засоряем проект
        # идея в том что токены живут долго, для тестов мы можем создать отдельный токен и захардкодить
        # но если что то поменяется, тесты все равно отработают корректно, а в консоли будет уведомление
        # токен проверяем не чаще чем раз в 10 секунд что бы не добавлять кучу новых запросов
        if time.time() - Endpoint.LAST_TOKEN_CHECK > 10:
            if not self.is_token_valid(Endpoint.AUTH_TOKEN):
                print(Fore.MAGENTA + "Срок действия токена истек - Получение нового токена - "
                                     "Желательно токен в классе Endpoint завести рабочий")
                Endpoint.AUTH_TOKEN = self.get_new_token()
            Endpoint.LAST_TOKEN_CHECK = time.time()

    def get_new_token(self):
        response = requests.post(f"{self.BASE_URL}/authorize", json=main_user)
        assert response.status_code == 200, f"При получении токена ожидали status_code 200 а получили {response.status_code}"
        return {"Authorization": response.json()["token"]}

    def is_token_valid(self, token):
        response = requests.get(f"{self.BASE_URL}/authorize/{token['Authorization']}")
        return response.status_code == 200

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
    def check_body_meme(self, correct_body):
        with allure.step(f"Проверяем структуру ответа"):
            required_fields = ["id", "info", "tags", "text", "updated_by", "url"]
            js = self.response.json()
            assert isinstance(js, dict), "В ответе не dict"
            for field in required_fields:
                assert field in js, f"У объекта id={js.get('id')} отсутствует обязательное поле {field}"
            assert isinstance(js['id'], int), f"Поле id не int\n{js}"

            assert isinstance(js['info'], dict), f"Поле info не dict\n{js}"
            assert js['info'] == correct_body['info'], f"Поле info содержит не те данные что отправили\n{js}"

            assert isinstance(js['tags'], list), f"Поле tags не list\n{js}"
            assert js['tags'] == correct_body['tags'], f"Поле tags содержит не те данные что отправили\n{js}"

            assert isinstance(js['text'], str), f"Поле text не str\n{js}"
            assert js['text'] == correct_body['text'], f"Поле text содержит не те данные что отправили\n{js}"

            assert isinstance(js['updated_by'], str), f"Поле updated_by не str\n{js}"
            assert js['updated_by'] == correct_body[
                'updated_by'], f"Поле updated_by содержит не те данные что отправили\n{js}"

            assert isinstance(js['url'], str), f"Поле url не str\n{js}"
            assert js['url'] == correct_body['url'], f"Поле url содержит не те данные что отправили\n{js}"

    @allure.step("Проверяем id в теле ответа")
    def check_id_meme(self, id_meme):
        js = self.response.json()
        assert js['id'] == id_meme, f"У мема некорректный id в теле\n{js}"

    @allure.step("Проверяем что дополнительное поле игнорируется")
    def check_no_additional_field(self):
        js = self.response.json()
        assert "TEST" not in js, "Появилось дополнительное поле 'TEST'"
