import allure
import pytest

correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
                "tags": ["cat", "bu"],
                "text": "Бу! испугался?!",
                "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}

bad_token = [None, {}, {"Authorization": "qwerty"}, {"Authorization": ""}]

bad_body_no_field = [{"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad_body"},
                     {"info": {"c": 111}, "tags": ["qqq"], "url": "https://test.ru"},
                     {"info": {"c": 111}, "text": "test_bad_body", "url": "https://test.ru"},
                     {"tags": ["qqq"], "text": "test_bad_body", "url": "https://test.ru"}]

bad_body_additional_field = {"info": {"c": 111},
                             "tags": ["qqq"],
                             "text": "test_bad_body",
                             "url": "https://test.ru",
                             "TEST": "TESTOVICH"}

bad_empty_body = [{}, None]

bad_body_type_field_negative = [
    {"info": "str, должен быть {}", "tags": ["qqq"], "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": "str, должен быть []", "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": 111, "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad", "url": ["https://test.ru"]}]


@allure.title("Создание мема с валидными данными")
def test_post_meme(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.create_new_mem(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(200)
    post_meme_and_delete_fixture.check_body_meme()


@allure.title("Получение созданного мема по id")
def test_post_meme_through_get(post_meme_and_delete_fixture, get_one_meme_fixture):
    post_meme_and_delete_fixture.create_new_mem(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    get_one_meme_fixture.get_meme(post_meme_and_delete_fixture.response.json()['id'],
                                  post_meme_and_delete_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    get_one_meme_fixture.check_body_meme()


@allure.title("Создание мема без токена/некорректный токен/пустой токен")
@pytest.mark.parametrize("badtoken", bad_token)
def test_post_meme_invalid_token(post_meme_and_delete_fixture, badtoken):
    post_meme_and_delete_fixture.create_new_mem(correct_body, badtoken)
    post_meme_and_delete_fixture.check_response_status_code(401)


@allure.title("Создание мема с дополнительным полем")
def test_post_meme_additional_field(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.create_new_mem(bad_body_additional_field, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(200)
    post_meme_and_delete_fixture.check_post_meme_no_additional_field()


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
    post_meme_and_delete_fixture.check_post_meme_invalid_method(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_response_status_code(405)


@allure.title("Время ответа при создании мема")
def test_post_meme_time_response(post_meme_and_delete_fixture):
    post_meme_and_delete_fixture.create_new_mem(correct_body, post_meme_and_delete_fixture.AUTH_TOKEN)
    post_meme_and_delete_fixture.check_time_response()
