import pytest
from endpoints.get_all_mems import GetAllMeme
from endpoints.post_mem import PostMem
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.put_meme import PutMeme
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize import GetAuthorized
from endpoints.base_endpoint import Endpoint
from data_for_tests import correct_body, two_akk_meme, main_user, two_user


@pytest.fixture()
def authorization_endpoint_post():
    """Экземпляр класса PostAuthorize"""
    obj = PostAuthorize()
    return obj


@pytest.fixture()
def authorization_endpoint_get():
    """Экземпляр класса GetAuthorized"""
    obj = GetAuthorized()
    return obj


@pytest.fixture()
def endpoint_get_all_meme():
    """Экземпляр класса GetAllMeme"""
    obj = GetAllMeme()
    return obj


@pytest.fixture()
def endpoint_get_one_meme():
    """Экземпляр класса GetMeme"""
    obj = GetMeme()
    return obj


@pytest.fixture()
def endpoint_post_meme():
    """Экземпляр класса PostMem"""
    obj = PostMem()
    return obj


@pytest.fixture()
def post_meme_and_delete_fixture(endpoint_delete_meme):
    """Экземпляр класса PostMem, удаление по id после"""
    obj = PostMem()
    yield obj
    if obj.response and obj.response.status_code == 200:
        endpoint_delete_meme.delete_meme(obj.response.json()['id'], obj.AUTH_TOKEN)


@pytest.fixture()
def endpoint_put_meme():
    """Экземпляр класса PutMeme"""
    obj = PutMeme()
    return obj


@pytest.fixture()
def endpoint_delete_meme():
    """Экземпляр класса DeleteMeme"""
    obj = DeleteMeme()
    return obj


@pytest.fixture()
def create_meme_id_fixture(endpoint_post_meme):
    """Создание мема, возврат id"""
    endpoint_post_meme.create_new_mem(correct_body, endpoint_post_meme.AUTH_TOKEN)
    meme_id = endpoint_post_meme.response.json()['id']
    return meme_id


@pytest.fixture()
def create_and_delete_meme_id_fixture(endpoint_post_meme, endpoint_delete_meme):
    """Создание мема, возврат id, удаление"""
    endpoint_post_meme.create_new_mem(correct_body, endpoint_post_meme.AUTH_TOKEN)
    meme_id = endpoint_post_meme.response.json()['id']
    yield meme_id
    endpoint_delete_meme.delete_meme(meme_id, endpoint_delete_meme.AUTH_TOKEN)


@pytest.fixture()
def other_user_meme_id(endpoint_post_meme, endpoint_delete_meme):
    """Создаем мем от AUTH_TOKEN2(2ой аккаунт), после удаляем мем"""
    endpoint_post_meme.create_new_mem(two_akk_meme, endpoint_post_meme.AUTH_TOKEN2)
    id_new_akk_meme = endpoint_post_meme.response.json()['id']
    yield id_new_akk_meme
    endpoint_delete_meme.delete_meme(id_new_akk_meme, endpoint_post_meme.AUTH_TOKEN2)


@pytest.fixture(scope="session", autouse=True)
def tokens():
    """Создаем токены для 2х аккаунтов"""
    auth = PostAuthorize()
    Endpoint.AUTH_TOKEN = {"Authorization": auth.post_authorize(main_user).json()["token"]}
    Endpoint.AUTH_TOKEN2 = {"Authorization": auth.post_authorize(two_user).json()["token"]}
