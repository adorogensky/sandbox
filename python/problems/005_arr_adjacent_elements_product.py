#!/usr/bin/python3
'''
Given an array of integers, find the pair of adjacent elements that 
has the largest product and return that product.

Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.
'''
import unittest

def solution(_arr):
    if _arr == None or len(_arr) < 2:
        return None

    arr_len = len(_arr)

    _max_product = None
    for i in range(0, arr_len - 1):
        _product = _arr[i] * _arr[i + 1]
        if _max_product == None or _max_product < _product:
            _max_product = _product 
    return _max_product

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([3, 6, -2, -5, 7, 3]), 21)
    def test_2(self):
        self.assertEqual(solution([-1, -2]), 2)
    def test_3(self):
        self.assertEqual(solution([5, 1, 2, 3, 1, 4]), 6)
    def test_3(self):
        self.assertEqual(solution([]), None)
    def test_4(self):
        self.assertEqual(solution([1]), None)
    def test_5(self):
        self.assertEqual(solution(None), None)

if __name__ == '__main__':
    unittest.main()

