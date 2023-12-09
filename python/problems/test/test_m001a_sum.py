'''
find sum of two numbers
'''

import sys
sys.path.append('..')
from m001a_sum import sum

def test_0_0():
    assert sum(0, 0) == 0

def test_1_n1():
    assert sum(1, -1) == 0

def test_1_1():
    assert sum(1, 1) == 2
