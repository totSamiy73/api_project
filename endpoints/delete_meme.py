from endpoints.base_endpoint import Endpoint
import requests
import allure


class DeleteMeme(Endpoint):

    @allure.step("Удаляем мем")
    def delete_meme(self, id_meme, token):
        self.response = requests.delete(f"{self.BASE_URL}/meme/{id_meme}", headers=token)

    @allure.step("Текст ответа при удалении мема")
    def check_text_meme(self, id_meme):
        assert self.response.text == f"Meme with id {id_meme} successfully deleted"

    @allure.step("Удаление мема через POST запрос")
    def check_delete_meme_invalid_method(self, id_meme, token):
        self.response = requests.post(f"{self.BASE_URL}/meme/{id_meme}", headers=token)
