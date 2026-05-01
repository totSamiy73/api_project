import allure
import pytest
from data_for_tests import bad_token


@allure.title("Получение всех мемов")
@pytest.mark.smoke
def test_get_all_meme(endpoint_get_all_meme):
    endpoint_get_all_meme.get_all_meme(endpoint_get_all_meme.AUTH_TOKEN)
    endpoint_get_all_meme.check_response_status_code(200)
    endpoint_get_all_meme.check_body_get_all_meme()


@allure.title("Получение всех мемов, без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_get_all_meme_invalid_token(endpoint_get_all_meme, badtoken):
    endpoint_get_all_meme.get_all_meme(badtoken)
    endpoint_get_all_meme.check_response_status_code(401)


@allure.title("Получение всех мемов при неверном методе запроса POST")
def test_get_all_meme_invalid_method(endpoint_get_all_meme):
    endpoint_get_all_meme.get_all_meme_invalid_method()
    endpoint_get_all_meme.check_response_status_code(405)


@allure.title("Время ответа при запросе всех мемов")
def test_get_all_meme_time_response(endpoint_get_all_meme):
    endpoint_get_all_meme.get_all_meme(endpoint_get_all_meme.AUTH_TOKEN)
    endpoint_get_all_meme.check_time_response()
