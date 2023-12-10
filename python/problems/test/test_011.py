"""
In an array of numbers find max sequence of 1s
"""
from p011_max_1s_seq import max_1s_seq

def test_01():
    assert max_1s_seq([]) == 0

def test_02():
    assert max_1s_seq([1]) == 1

def test_03():
    assert max_1s_seq([1, 1]) == 2

def test_04():
    assert max_1s_seq([0, 0]) == 0

def test_05():
    assert max_1s_seq([0, 0, 1]) == 1

def test_06():
    assert max_1s_seq([0, 0, 1, 2, 2, 1, 1, 1]) == 3
