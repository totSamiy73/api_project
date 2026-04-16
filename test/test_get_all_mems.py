import allure
import pytest

bad_token = [None, {}, {"Authorization": "qwerty"}, {"Authorization": ""}]


@allure.title("Получение всех мемов")
def test_get_all_meme_status_positive(get_all_meme_fixture):
    get_all_meme_fixture.get_all_meme(get_all_meme_fixture.AUTH_TOKEN)
    get_all_meme_fixture.check_response_status_code(200)
    get_all_meme_fixture.check_body_get_all_meme()


@allure.title("Получение всех мемов, без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_get_all_meme_unauthorized(get_all_meme_fixture, badtoken):
    get_all_meme_fixture.get_all_meme(badtoken)
    get_all_meme_fixture.check_response_status_code(401)


@allure.title("Получение всех мемов при неверном методе запроса POST")
def test_get_all_meme_invalid_method(get_all_meme_fixture):
    get_all_meme_fixture.get_all_meme_invalid_method()
    get_all_meme_fixture.check_response_status_code(405)


@allure.title("Время ответа при запросе всех мемов")
def test_get_all_meme_time_response(get_all_meme_fixture):
    get_all_meme_fixture.get_all_meme(get_all_meme_fixture.AUTH_TOKEN)
    get_all_meme_fixture.get_all_meme_time_response()
