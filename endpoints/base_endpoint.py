import allure


class Endpoint:
    BASE_URL = "http://memesapi.course.qa-practice.com"
    AUTH_TOKEN = {"Authorization": "IGhQfTB49JgOFxT"}
    response = None

    @allure.step("Статус код ответа")
    def check_response_status_code(self, status_code):
        with allure.step(f"Проверяем статус код {status_code}"):
            actual_sc = self.response.status_code
            assert actual_sc == status_code, f"неверный статус код, ожидали {status_code}, получили {actual_sc}"
