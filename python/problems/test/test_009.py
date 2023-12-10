'''
find the max product of 2 adjacent elements in an array
e.g.
 [3, 6, -2, -5, 7, 3] should return 21
'''
from p009_max_product import max_product

def test_1():
    assert max_product([3, 6, -2, -5, 7, 3]) == 21

def test_2():
    assert max_product([-1, -2]) == 2

def test_3():
    assert max_product([5, 1, 2, 3, 1, 4]) == 6

def test_4():
    assert max_product([]) == None

def test_5():
    assert max_product([1]) == None
