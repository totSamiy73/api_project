import allure
import pytest
from data_for_tests import bad_token, correct_body, two_akk_meme


@allure.title("Получение мема по id")
def test_get_one_meme(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    body = correct_body.copy()
    body['updated_by'] = 'tot'  # добавили updated_by для сравнения с ответом
    get_one_meme_fixture.check_body_meme(body)
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


@allure.title("Получение чужого мема по id")
def test_get_meme_someone(get_one_meme_fixture, token_create_meme_create_and_delete_return_id):
    get_one_meme_fixture.get_meme(token_create_meme_create_and_delete_return_id, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    body = two_akk_meme.copy()
    body['updated_by'] = 'test_two_akk'  # добавили updated_by для сравнения с ответом
    get_one_meme_fixture.check_body_meme(body)
