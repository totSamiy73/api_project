import allure
import pytest

correct_body_put = {
    "info": {"test": 123},
    "tags": ["тест", "test", 123],
    "text": "qwerty",
    "url": "https://cdn.idaprikol.ru/images/06649808945b67047d041fbc91224c909318237db00aa10efae5ae8de721e6b5_1.jpg"}

bad_token = [None, {}, {"Authorization": "qwerty"}, {"Authorization": ""}]

bad_body_additional_field = {"info": {"c": 111},
                             "tags": ["qqq"],
                             "text": "test_bad_body",
                             "url": "https://test.ru",
                             "TEST": "TESTOVICH"}

bad_body_no_field = [{"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad_body"},
                     {"info": {"c": 111}, "tags": ["qqq"], "url": "https://test.ru"},
                     {"info": {"c": 111}, "text": "test_bad_body", "url": "https://test.ru"},
                     {"tags": ["qqq"], "text": "test_bad_body", "url": "https://test.ru"}]

bad_empty_body = [{}, None]

bad_body_type_field_negative = [
    {"info": "str, должен быть {}", "tags": ["qqq"], "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": "str, должен быть []", "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": 111, "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad", "url": ["https://test.ru"]}]

@allure.title("Обновление мема с валидными данными")
def test_put_meme(put_meme_fixture, create_and_delete_meme_id_fixture, get_one_meme_fixture):
    body = correct_body_put.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(200)
    put_meme_fixture.check_body_meme(body)
    put_meme_fixture.check_id_meme(create_and_delete_meme_id_fixture)
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    get_one_meme_fixture.check_body_meme(body)
    get_one_meme_fixture.check_id_meme(create_and_delete_meme_id_fixture)

@allure.title("Обновление мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_put_meme_invalid_token(put_meme_fixture, create_and_delete_meme_id_fixture, badtoken):
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, correct_body_put, badtoken)
    put_meme_fixture.check_response_status_code(401)

@allure.title("Обновление мема с дополнительным полем")
def test_put_meme_additional_field(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = bad_body_additional_field.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(200)
    body.pop("TEST")
    put_meme_fixture.check_body_meme(body)
    put_meme_fixture.check_meme_no_additional_field()

@allure.title("Обновление мема без обязательных полей")
@pytest.mark.parametrize("badbody_no_field", bad_body_no_field)
def test_put_meme_without_url_text_tags_info(put_meme_fixture, create_and_delete_meme_id_fixture, badbody_no_field):
    body = badbody_no_field.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)

@allure.title("Обновление мема без обязательного поля id")
def test_put_meme_without_id(put_meme_fixture, create_and_delete_meme_id_fixture):
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, correct_body_put, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)


@allure.title("Обновление мема с пустым и отсутствующим телом")
@pytest.mark.parametrize("badempty_body", bad_empty_body)
def test_put_meme_empty_body(put_meme_fixture, create_and_delete_meme_id_fixture, badempty_body):
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, badempty_body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)

@allure.title("Обновление мема c невалидным типом данных полей")
@pytest.mark.parametrize("bad_body_type_field", bad_body_type_field_negative)
def test_put_meme_type_field_negative(put_meme_fixture, create_and_delete_meme_id_fixture, bad_body_type_field):
    body = bad_body_type_field.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)

@allure.title("Обновление мема c невалидным типом данных поля id")
def test_put_meme_type_id_negative(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = correct_body_put.copy()
    body['id'] = [create_and_delete_meme_id_fixture]
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)

@allure.title("Обновление мема через метод POST")
def test_put_meme_invalid_method_post(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = correct_body_put.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme_invalid_method(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(405)

@allure.title("Обновление мема id body != id url")
def test_put_meme_id_mismatch(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = correct_body_put.copy()
    body['id'] = create_and_delete_meme_id_fixture + 1
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(400)

@allure.title("Обновление мема с несуществующим id")
def test_non_existent_id_put_meme(put_meme_fixture):
    body = correct_body_put.copy()
    body['id'] = 1234567890
    put_meme_fixture.put_meme(body['id'], body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(404)

@allure.title("Обновление мема с некорректным id")
def test_put_meme_invalid_id(put_meme_fixture):
    body = correct_body_put.copy()
    body['id'] = "qwerty"
    put_meme_fixture.put_meme(body['id'], body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_response_status_code(404)

@allure.title("Повторный PUT возвращает тот же результат")
def test_double_put_meme(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = correct_body_put.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.check_double_put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)


@allure.title("Время ответа при обновлении мема")
def test_put_meme_time_response(put_meme_fixture, create_and_delete_meme_id_fixture):
    body = correct_body_put.copy()
    body['id'] = create_and_delete_meme_id_fixture
    put_meme_fixture.put_meme(create_and_delete_meme_id_fixture, body, put_meme_fixture.AUTH_TOKEN)
    put_meme_fixture.check_time_response()

# не забыть добавить тест на обновление чужего мема



