def factorial(n: int) -> int:
    if n == 0: return 1 else return n * factorial(n - 1)

def test_0():
    assert factorial(0) == 1

def test_1():
    assert factorial(1) == 1

def test_2():
    assert factorial(2) == 2

def test_3():
    assert factorial(3) == 6
