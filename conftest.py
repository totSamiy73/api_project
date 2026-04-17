import pytest
import requests
from endpoints.get_all_mems import GetAllMeme
from endpoints.post_mem import PostMem
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme

correct_body = {"info": {"colors": ["green", "black", "white"], "objects": ["picture", "text"]},
                "tags": ["cat", "bu"],
                "text": "Бу! испугался?!",
                "url": "https://spbcult.ru/upload/iblock/7b9/9n0tc4etzlpw3t1h1021gjzhwl226j5k.jpg"}


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
