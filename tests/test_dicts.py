from utils.dicts import get_val
import pytest

@pytest.fixture
def diction():
    return {'key': 'value'}


def test_get_val(diction):
    assert get_val({'key': 'value'}, 'key') == 'value'
    assert get_val({'key': 'value'}, 'key', 'git') == 'value'
    assert get_val({}, 'key', 'git') == 'git'
    assert get_val({}, 'key', 'hello') == 'hello'
    assert get_val({'key':'value'}, 'key11', 'git') == 'git'

