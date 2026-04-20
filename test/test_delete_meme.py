import allure
import pytest
from data_for_tests import bad_token


@allure.title("Удаление существующего мема по id")
@pytest.mark.smoke
def test_delete_meme(create_meme_id_fixture, delete_meme_fixture, get_one_meme_fixture):
    delete_meme_fixture.delete_meme(create_meme_id_fixture, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(200)
    delete_meme_fixture.check_text_meme(create_meme_id_fixture)
    get_one_meme_fixture.get_meme(create_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(404)


@allure.title("Повторное удаление уже удалённого мема")
def test_double_delete_meme(create_meme_id_fixture, delete_meme_fixture):
    delete_meme_fixture.delete_meme(create_meme_id_fixture, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(200)
    delete_meme_fixture.delete_meme(create_meme_id_fixture, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(404)


@allure.title("Удаление мема с несуществующим id")
def test_non_existent_delete_meme(delete_meme_fixture):
    delete_meme_fixture.delete_meme(1234567890, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(404)


@allure.title("Удаление мема с некорректным id")
def test_delete_meme_invalid_id(delete_meme_fixture):
    delete_meme_fixture.delete_meme(-1, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(404)


@allure.title("Удаление мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_delete_meme_invalid_token(create_and_delete_meme_id_fixture, delete_meme_fixture, badtoken):
    delete_meme_fixture.delete_meme(create_and_delete_meme_id_fixture, badtoken)
    delete_meme_fixture.check_response_status_code(401)


@allure.title("Удаление мема через метод POST")
def test_delete_meme_invalid_method_post(create_and_delete_meme_id_fixture, delete_meme_fixture):
    delete_meme_fixture.delete_meme_invalid_method(create_and_delete_meme_id_fixture,
                                                   delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(405)


@allure.title("Время ответа при удалении мема")
def test_delete_meme_time_response(create_meme_id_fixture, delete_meme_fixture):
    delete_meme_fixture.delete_meme(create_meme_id_fixture, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_time_response()


@allure.title("Удаление чужого мема")
def test_delete_meme_someone(for_two_akk_create_meme_and_delete_return_id, delete_meme_fixture):
    delete_meme_fixture.delete_meme(for_two_akk_create_meme_and_delete_return_id, delete_meme_fixture.AUTH_TOKEN)
    delete_meme_fixture.check_response_status_code(403)
