'''
find how many numbers are needed to form an integer range from given array
e.g.
  [0, 3] should return 2 (missing elements 1 and 2)
  [6, 2, 3, 8] should return 3 (missing elements are 4, 5 and 7)
  [5, 4, 6] should return 0 (no missin
'''
from p010_missed_range_numbers import missed_range_numbers

def test_1():
    assert missed_range_numbers([6, 2, 3, 8]) == 3

def test_2():
    assert missed_range_numbers([0, 3]) == 2

def test_3():
    assert missed_range_numbers([5, 4, 6]) == 0
