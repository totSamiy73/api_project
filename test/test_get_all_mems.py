import allure
import pytest

bad_token = [{}, {"Authorization": "qwerty"}, {"Authorization": ""}]


@allure.title("Получение всех мемов")
def test_get_all_mems_status_positive(get_all_mems_fixture):
    get_all_mems_fixture.get_all_mems(get_all_mems_fixture.AUTH_TOKEN)
    get_all_mems_fixture.check_response_status_code(200)
    get_all_mems_fixture.check_body_get_all_mems()


@allure.title("Получение всех мемов, без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_get_all_mems_unauthorized(get_all_mems_fixture, badtoken):
    get_all_mems_fixture.get_all_mems(badtoken)
    get_all_mems_fixture.check_response_status_code(401)


@allure.title("Получение всех мемов при неверном методе запроса(post)")
def test_get_all_mems_post_negative(get_all_mems_fixture):
    get_all_mems_fixture.get_all_mems_post_negative()
    get_all_mems_fixture.check_response_status_code(405)


@allure.title("Время ответа при запросе всех мемов")
def test_get_all_mems_time_response(get_all_mems_fixture):
    get_all_mems_fixture.get_all_mems(get_all_mems_fixture.AUTH_TOKEN)
    get_all_mems_fixture.get_all_mems_time_response()
