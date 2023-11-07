#!/usr/bin/python3
import unittest

def solution(_str):
    str_len = len(_str)
    for i in range(0, str_len // 2):
        if _str[i] != _str[str_len - 1 - i]:
            return False
    return True

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(solution('eye'))
    def test_2(self):
        self.assertTrue(solution('noon'))
    def test_3(self):
        self.assertTrue(solution('decaf faced'))
    def test_4(self):
        self.assertFalse(solution('taco cat'))
    def test_5(self):
        self.assertFalse(solution('racecars'))

if __name__ == '__main__':
    unittest.main()
