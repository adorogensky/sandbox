'''
  find max unique element in array, return -1 if not found
  e.g.
  [1, 2, 1, 2] should return -1
  [1, 3, 3, 2, 2] should return 1
  [1, 1, 3, 4, 4] should return 3
  [1, 1, 7, 6, 6, 7, 5] should return 5
'''
from p012_max_unique import max_unique

def test_01():
    assert max_unique([1, 2, 1, 2]) == -1

def test_02():
    assert max_unique([1, 3, 3, 2, 2]) == 1

def test_03():
    assert max_unique([1, 1, 3, 4, 4]) == 3

def test_04():
    assert max_unique([1, 1, 7, 6, 6, 7, 5]) == 5
