import allure
import pytest
from data_for_tests import bad_empty_body, two_user


@allure.title("Авторизация пользователя с валидными данными")
@pytest.mark.smoke
def test_post_authorize(post_authorize_fixture):
    post_authorize_fixture.post_authorize(two_user)
    post_authorize_fixture.check_response_status_code(200)
    post_authorize_fixture.check_body_post_authorize(two_user)


@allure.title("Авторизация пользователя с невалидным типом данных в поле name")
def test_post_authorize_type_name_negative(post_authorize_fixture):
    post_authorize_fixture.post_authorize({"name": [123]})
    post_authorize_fixture.check_response_status_code(400)


@allure.title("Авторизация пользователя с пустым и отсутствующим телом запроса")
@pytest.mark.parametrize("badempty_body", bad_empty_body)
def test_post_authorize_empty_body(post_authorize_fixture, badempty_body):
    post_authorize_fixture.post_authorize(badempty_body)
    post_authorize_fixture.check_response_status_code(400)


@allure.title("Авторизация пользователя через метод PUT")
def test_post_authorize_invalid_method(post_authorize_fixture):
    post_authorize_fixture.post_authorize_invalid_method(two_user)
    post_authorize_fixture.check_response_status_code(405)
