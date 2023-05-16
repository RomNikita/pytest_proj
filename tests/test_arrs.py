from utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], 0, "test") == "test"
    assert get([1,2,3,4], -1, "test") == "test"
    assert get([1,2,3], 0) == 1
    assert get([], 3) == None
    assert get([], -1) == None
    assert get([1,2,3], int()) == 1


def test_my_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([1,2,3,4], -1) == [4]
    assert my_slice([], 0) == []
    assert my_slice([1,2,3], 4) == []
    assert my_slice([1,2,3], 0, 2) == [1,2]
    assert my_slice([1, 2, 3], -1, -2) == []
    assert my_slice([1, 2, 3], 0, -2) == [1]
    assert my_slice([]) == []
    assert my_slice([], 0, 2) == []
    assert my_slice([1, 2, 3], 0) == [1, 2, 3]
    assert my_slice([1, 2, 3], -6) == [1, 2, 3]