#!/usr/local/bin/pytest -s
import pytest

@pytest.fixture(scope = 'function')
def test_setup(request):
    print("test setup")

    def test_teardown():
        print("test teardown")

    request.addfinalizer(test_teardown)

    return 1

def test_1(test_setup):
    assert test_setup == 1
    print("test 1")

def test_2(test_setup):
    assert test_setup == 1
    print("test 2")
