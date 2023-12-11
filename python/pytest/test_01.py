import pytest

@pytest.fixture(scope = 'function')
def linkedList(request):
    return [1, 2, 3]

def test_1(linkedList):
    assert linkedList == [1, 2, 3]
    del linkedList[0]
    assert linkedList == [2, 3]

def test_2(linkedList):
    assert linkedList == [1, 2, 3]
