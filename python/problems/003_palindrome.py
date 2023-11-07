#!/usr/bin/python3
import unittest

'''
Given the string, check if it is a palindrome, i.e.
a string that doesn't change when reversed, i.e.
it reads the same backward and forward

Examples:
"eye" is a palindrome
"noon" is a palindrome
"decaf faced" is a palindrome
"taco cat" is not a palindrome (backwards it spells "tac ocat")
"racecars" is not a palindrome (backwards it spells "sracecar")
'''
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
