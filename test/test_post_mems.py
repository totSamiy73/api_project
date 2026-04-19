import allure
import pytest
from data_for_tests import correct_body, bad_token, bad_body_no_field, bad_body_additional_field, bad_empty_body, \
    bad_body_type_field_negative


@allure.title("Создание мема с валидными данными")
def test_post_meme(post_meme_and_delete_fixture, get_one_meme_fixture):
    post_meme_and_delete_fixture.create_new_mem(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(200)
    body = correct_body.copy()
    body['updated_by'] = 'tot'  # добавили updated_by для сравнения с ответом
    post_meme_and_delete_fixture.check_body_meme(body)
    get_one_meme_fixture.get_meme(post_meme_and_delete_fixture.response.json()['id'],
                                  post_meme_and_delete_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    get_one_meme_fixture.check_body_meme(body)


@allure.title("Создание мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_post_meme_invalid_token(post_meme_and_delete_fixture, badtoken):
    post_meme_and_delete_fixture.create_new_mem(correct_body, badtoken)
    post_meme_and_delete_fixture.check_response_status_code(401)


@allure.title("Создание мема с дополнительным полем")
def test_post_meme_additional_field(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.create_new_mem(bad_body_additional_field, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(200)
    body = bad_body_additional_field.copy()
    body['updated_by'] = 'tot'
    post_meme_and_delete_fixture.check_body_meme(body)
    post_meme_and_delete_fixture.check_no_additional_field()


@allure.title("Создание мема без обязательных полей")
@pytest.mark.parametrize("badbody_no_field", bad_body_no_field)
def test_post_meme_without_url_text_tags_info(post_meme_and_delete_fixture, badbody_no_field):
    post_meme_and_delete_fixture.create_new_mem(badbody_no_field, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(400)


@allure.title("Создание мема с пустым и отсутствующим телом")
@pytest.mark.parametrize("badempty_body", bad_empty_body)
def test_post_meme_empty_body(post_meme_and_delete_fixture, badempty_body):
    post_meme_and_delete_fixture.create_new_mem(badempty_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(400)


@allure.title("Создание мема c невалидным типом данных полей")
@pytest.mark.parametrize("bad_body", bad_body_type_field_negative)
def test_post_meme_type_field_negative(post_meme_and_delete_fixture, bad_body):
    post_meme_and_delete_fixture.create_new_mem(bad_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(400)


@allure.title("Создание мема через метод PUT")
def test_post_meme_invalid_method_put(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.post_meme_invalid_method(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(405)


@allure.title("Время ответа при создании мема")
def test_post_meme_time_response(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.create_new_mem(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_time_response()
