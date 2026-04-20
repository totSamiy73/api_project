import pytest
import requests
from endpoints.get_all_mems import GetAllMeme
from endpoints.post_mem import PostMem
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.put_meme import PutMeme
from endpoints.post_authorize import PostAuthorize
from endpoints.get_authorize import GetAuthorized
from data_for_tests import correct_body, two_akk_meme


@pytest.fixture()
def post_authorize_fixture():
    """Экземпляр класса PostAuthorize"""
    obj = PostAuthorize()
    return obj


@pytest.fixture()
def get_authorize_fixture():
    """Экземпляр класса GetAuthorized"""
    obj = GetAuthorized()
    return obj


@pytest.fixture()
def get_all_meme_fixture():
    """Экземпляр класса GetAllMeme"""
    obj = GetAllMeme()
    return obj


@pytest.fixture()
def get_one_meme_fixture():
    """Экземпляр класса GetMeme"""
    obj = GetMeme()
    return obj


@pytest.fixture()
def post_meme_fixture():
    """Экземпляр класса PostMem"""
    obj = PostMem()
    return obj


@pytest.fixture()
def post_meme_and_delete_fixture():
    """Экземпляр класса PostMem, удаление по id после"""
    obj = PostMem()
    yield obj
    if obj.response and obj.response.status_code == 200:
        requests.delete(f"{obj.BASE_URL}/meme/{obj.response.json()['id']}", headers=obj.AUTH_TOKEN)


@pytest.fixture()
def put_meme_fixture():
    """Экземпляр класса PutMeme"""
    obj = PutMeme()
    return obj


@pytest.fixture()
def delete_meme_fixture():
    """Экземпляр класса DeleteMeme"""
    obj = DeleteMeme()
    return obj


@pytest.fixture()
def create_meme_id_fixture(post_meme_fixture):
    """Создание мема, возврат id"""
    post_meme_fixture.create_new_mem(correct_body, post_meme_fixture.AUTH_TOKEN)
    meme_id = post_meme_fixture.response.json()['id']
    return meme_id


@pytest.fixture()
def create_and_delete_meme_id_fixture(post_meme_fixture, delete_meme_fixture):
    """Создание мема, возврат id, удаление"""
    post_meme_fixture.create_new_mem(correct_body, post_meme_fixture.AUTH_TOKEN)
    meme_id = post_meme_fixture.response.json()['id']
    yield meme_id
    delete_meme_fixture.delete_meme(meme_id, delete_meme_fixture.AUTH_TOKEN)


@pytest.fixture()
def for_two_akk_create_meme_and_delete_return_id(post_meme_fixture, delete_meme_fixture):
    """Создаем мем от AUTH_TOKEN2(2ой аккаунт), после удаляем мем"""
    post_meme_fixture.create_new_mem(two_akk_meme, post_meme_fixture.AUTH_TOKEN2)
    id_new_akk_meme = post_meme_fixture.response.json()['id']
    yield id_new_akk_meme
    delete_meme_fixture.delete_meme(id_new_akk_meme, post_meme_fixture.AUTH_TOKEN2)
