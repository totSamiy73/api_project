import allure

@allure.title("Получение мема по id")
def test_get_meme(get_one_meme_fixture, create_and_delete_meme_id_fixture):
    get_one_meme_fixture.get_meme(create_and_delete_meme_id_fixture, get_one_meme_fixture.AUTH_TOKEN)
    get_one_meme_fixture.check_response_status_code(200)
    get_one_meme_fixture.check_body_meme()


