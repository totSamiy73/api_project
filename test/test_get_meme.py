import allure
import pytest
from data_for_tests import bad_token, correct_body, two_akk_meme


@allure.title("Получение мема по id")
@pytest.mark.smoke
def test_get_one_meme(endpoint_get_one_meme, create_and_delete_meme_id_fixture):
    endpoint_get_one_meme.get_meme(create_and_delete_meme_id_fixture, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(200)
    body = correct_body.copy()
    body['updated_by'] = 'tot'  # добавили updated_by для сравнения с ответом
    endpoint_get_one_meme.check_body_meme(body)
    endpoint_get_one_meme.check_id_meme(create_and_delete_meme_id_fixture)


@allure.title("Повторный GET возвращает тот же результат")
def test_double_get_meme(endpoint_get_one_meme, create_and_delete_meme_id_fixture):
    endpoint_get_one_meme.check_double_get_meme(create_and_delete_meme_id_fixture, endpoint_get_one_meme.AUTH_TOKEN)


@allure.title("Получение мема с несуществующим id")
def test_non_existent_id_get_one_meme(endpoint_get_one_meme):
    endpoint_get_one_meme.get_meme(1234567890, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(404)


@allure.title("Получение мема с некорректным id")
def test_get_one_meme_invalid_id(endpoint_get_one_meme):
    endpoint_get_one_meme.get_meme("onetwothree", endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(404)


@allure.title("Получение мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_get_one_meme_invalid_token(endpoint_get_one_meme, create_and_delete_meme_id_fixture, badtoken):
    endpoint_get_one_meme.get_meme(create_and_delete_meme_id_fixture, badtoken)
    endpoint_get_one_meme.check_response_status_code(401)


@allure.title("Получение мема через метод POST")
def test_get_one_meme_invalid_method_post(endpoint_get_one_meme, create_and_delete_meme_id_fixture):
    endpoint_get_one_meme.get_meme_invalid_method(create_and_delete_meme_id_fixture, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(405)


@allure.title("Время ответа при получении мема")
def test_get_one_meme_time_response(endpoint_get_one_meme, create_and_delete_meme_id_fixture):
    endpoint_get_one_meme.get_meme(create_and_delete_meme_id_fixture, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_time_response()


@allure.title("Получение чужого мема по id")
def test_get_meme_someone(endpoint_get_one_meme, other_user_meme_id):
    endpoint_get_one_meme.get_meme(other_user_meme_id, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(200)
    body = two_akk_meme.copy()
    body['updated_by'] = 'test_two_akk'  # добавили updated_by для сравнения с ответом
    endpoint_get_one_meme.check_body_meme(body)
