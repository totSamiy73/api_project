import pytest
import requests
from endpoints.get_all_mems import GetAllMems


@pytest.fixture()
def get_all_mems_fixture():
    obj = GetAllMems()
    return obj
