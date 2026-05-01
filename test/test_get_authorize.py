import allure
import pytest
from data_for_tests import bad_token_for_get_authorize


@allure.title('Проверка активного токена')
@pytest.mark.smoke
def test_get_authorize(authorization_endpoint_get):
    authorization_endpoint_get.get_authorize_token()
    authorization_endpoint_get.check_response_status_code(200)
    authorization_endpoint_get.check_text_get_authorize_token()


@allure.title('Проверка некорректного токена')
@pytest.mark.parametrize("bad_token", bad_token_for_get_authorize)
def test_get_authorize_not_exists(authorization_endpoint_get, bad_token):
    authorization_endpoint_get.get_authorize_token(bad_token)
    authorization_endpoint_get.check_response_status_code(404)


@allure.title("Проверка активного токена через метод POST")
def test_get_authorize_invalid_method(authorization_endpoint_get):
    authorization_endpoint_get.get_authorize_invalid_method()
    authorization_endpoint_get.check_response_status_code(405)


@allure.title("Время ответа активноcти токена")
def test_get_authorize_time_response(authorization_endpoint_get):
    authorization_endpoint_get.get_authorize_token()
    authorization_endpoint_get.check_time_response()
