from utils.dicts import get_val

def test_get_val():
    assert get_val({'key': 'value'}, 'key') == 'value'
    assert get_val({'key': 'value'}, 'key', 'git') == 'value'
    assert get_val({}, 'key', 'git') == 'git'
    assert get_val({}, 'key', 'hello') == 'hello'
    assert get_val({'key':'value'}, 'key11', 'git') == 'git'

