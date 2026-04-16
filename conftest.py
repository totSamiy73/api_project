import pytest
import requests
from endpoints.get_all_mems import GetAllMeme
from endpoints.post_mem import PostMem


@pytest.fixture()
def get_all_meme_fixture():
    obj = GetAllMeme()
    return obj

@pytest.fixture()
def post_meme_fixture():
    obj = PostMem()
    yield obj
    if obj.response and obj.response.status_code == 200:
        requests.delete(f"{obj.BASE_URL}/meme/{obj.response.json()['id']}", headers=obj.AUTH_TOKEN)
