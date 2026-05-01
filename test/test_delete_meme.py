import allure
import pytest
from data_for_tests import bad_token


@allure.title("Удаление существующего мема по id")
@pytest.mark.smoke
def test_delete_meme(create_meme_id_fixture, endpoint_delete_meme, endpoint_get_one_meme):
    endpoint_delete_meme.delete_meme(create_meme_id_fixture, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(200)
    endpoint_delete_meme.check_text_response_upon_deletion(create_meme_id_fixture)
    endpoint_get_one_meme.get_meme(create_meme_id_fixture, endpoint_get_one_meme.AUTH_TOKEN)
    endpoint_get_one_meme.check_response_status_code(404)


@allure.title("Повторное удаление уже удалённого мема")
def test_double_delete_meme(create_meme_id_fixture, endpoint_delete_meme):
    endpoint_delete_meme.delete_meme(create_meme_id_fixture, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(200)
    endpoint_delete_meme.delete_meme(create_meme_id_fixture, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(404)


@allure.title("Удаление мема с несуществующим id")
def test_non_existent_delete_meme(endpoint_delete_meme):
    endpoint_delete_meme.delete_meme(1234567890, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(404)


@allure.title("Удаление мема с некорректным id")
def test_delete_meme_invalid_id(endpoint_delete_meme):
    endpoint_delete_meme.delete_meme(-1, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(404)


@allure.title("Удаление мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_delete_meme_invalid_token(create_and_delete_meme_id_fixture, endpoint_delete_meme, badtoken):
    endpoint_delete_meme.delete_meme(create_and_delete_meme_id_fixture, badtoken)
    endpoint_delete_meme.check_response_status_code(401)


@allure.title("Удаление мема через метод POST")
def test_delete_meme_invalid_method_post(create_and_delete_meme_id_fixture, endpoint_delete_meme):
    endpoint_delete_meme.delete_meme_invalid_method(create_and_delete_meme_id_fixture,
                                                   endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(405)


@allure.title("Время ответа при удалении мема")
def test_delete_meme_time_response(create_meme_id_fixture, endpoint_delete_meme):
    endpoint_delete_meme.delete_meme(create_meme_id_fixture, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_time_response()


@allure.title("Удаление чужого мема")
def test_delete_meme_someone(other_user_meme_id, endpoint_delete_meme):
    endpoint_delete_meme.delete_meme(other_user_meme_id, endpoint_delete_meme.AUTH_TOKEN)
    endpoint_delete_meme.check_response_status_code(403)
