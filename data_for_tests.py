correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
                "tags": ["cat", "bu"],
                "text": "Бу! испугался?!",
                "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}

two_akk_meme = {"info": {"q": 1}, "tags": [], "text": "akk2", "url": ""}

bad_token = [None, {}, {"Authorization": "qwerty"}, {"Authorization": ""}]

bad_token_for_get_authorize = ["", "qwerty123456789", "qwerty_!@$%^&*(-", 123456789012345]

main_user = {"name": "tot"}

two_user = {"name": "test_two_akk"}

bad_empty_body = [{}, None]

bad_body_no_field = [{"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad_body"},
                     {"info": {"c": 111}, "tags": ["qqq"], "url": "https://test.ru"},
                     {"info": {"c": 111}, "text": "test_bad_body", "url": "https://test.ru"},
                     {"tags": ["qqq"], "text": "test_bad_body", "url": "https://test.ru"}]

bad_body_additional_field = {"info": {"c": 111},
                             "tags": ["qqq"],
                             "text": "test_bad_body",
                             "url": "https://test.ru",
                             "TEST": "TESTOVICH"}

bad_body_type_field_negative = [
    {"info": "str, должен быть {}", "tags": ["qqq"], "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": "str, должен быть []", "text": "test_bad", "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": 111, "url": "https://test.ru"},
    {"info": {"c": 111}, "tags": ["qqq"], "text": "test_bad", "url": ["https://test.ru"]}]

correct_body_put = {
    "info": {"test": 123},
    "tags": ["тест", "test", 123],
    "text": "qwerty",
    "url": "https://cdn.idaprikol.ru/images/06649808945b67047d041fbc91224c909318237db00aa10efae5ae8de721e6b5_1.jpg"}
