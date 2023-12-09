import sys
sys.path.append('..')
from m002b_factorial import factorial
def test_0():
    assert factorial(0) == 1

def test_1():
    assert factorial(1) == 1

def test_2():
    assert factorial(2) == 2

def test_3():
    assert factorial(3) == 6
