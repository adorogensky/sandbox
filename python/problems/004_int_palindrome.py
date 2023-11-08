#!/usr/bin/python3
import unittest

'''
Check if a integer is a palindrome, i.e.
when it reads the same backward and forward

Examples:
1 is a palindrome
12 is NOT a palindrome
22 is a palindrome
212 is a palindrome
'''
def solution(_int):
    if _int < 10:
        return True
   
    _int_digits = []
    _int_digits.append(_int % 10)
    _int = _int // 10

    while True:
        if _int < 10:
            _int_digits.append(_int)
            break
        else:
            _int_digits.append(_int % 10)
            _int = _int // 10

    _int_digits_len = len(_int_digits)
    for i in range(0, _int_digits_len // 2):
        if _int_digits[i] != _int_digits[_int_digits_len - 1 - i]:
            return False
    
    return True

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(solution(1))
    def test_2(self):
        self.assertFalse(solution(12))
    def test_3(self):
        self.assertTrue(solution(22))
    def test_4(self):
        self.assertTrue(solution(212))

if __name__ == '__main__':
    unittest.main()
