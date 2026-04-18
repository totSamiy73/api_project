import allure
import pytest


bad_token = [None, {}, {"Authorization": "qwerty"}, {"Authorization": ""}]

correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
                "tags": ["cat", "bu"],
                "text": "Бу! испугался?!",
                "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}

@allure.title("Получение мема по id")
def test_get_one_meme(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    get_one_meme_fixture.check_body_meme(correct_body)
    get_one_meme_fixture.check_id_meme(create_and_delete_meme_id_fixture)

@allure.title("Повторный GET возвращает тот же результат")
def test_double_get_meme(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.check_double_get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)


@allure.title("Получение мема с несуществующим id")
def test_non_existent_id_get_one_meme(get_one_meme_fixture):
    get_one_meme_fixture.get_meme(1234567890, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(404)

@allure.title("Получение мема с некорректным id")
def test_get_one_meme_invalid_id(get_one_meme_fixture):
    get_one_meme_fixture.get_meme("onetwothree", get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(404)

@allure.title("Получение мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_get_one_meme_invalid_token(get_one_meme_fixture, create_and_delete_meme_id_fixture, badtoken):
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, badtoken)
    get_one_meme_fixture.check_response_status_code(401)

@allure.title("Получение мема через метод POST")
def test_get_one_meme_invalid_method_post(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.get_meme_invalid_method(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(405)

@allure.title("Время ответа при получении мема")
def test_get_one_meme_time_response(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_time_response()

# нужен тест на получение не только своего мема но и чужого

