#!/usr/bin/python3
import unittest

'''
Check if a string is a palindrome, i.e.
when it reads the same backward and forward (excluding spaces)

Examples:
"eye" is a palindrome
"noon" is a palindrome
"decaf faced" is a palindrome
"taco cat" is a palindrome (it spells "tacocat" backwards excluding spaces)
"racecars" is not a palindrome ("racecars" != "sracecar")
"borrow or rob" is a palindrome ("borrow or rob" == "borroworrob")
'''
def solution(_str):
    _str_no_spaces = _str.replace(" ", "")
    str_len = len(_str_no_spaces)
    for i in range(0, str_len // 2):
        if _str_no_spaces[i] != _str_no_spaces[str_len - 1 - i]:
            return False
    return True

def solution2(_str):
    str_len = len(_str)
    leftIdx = 0
    rightIdx = str_len - 1

    while leftIdx <= rightIdx:
        if _str[leftIdx] != ' ' and _str[rightIdx] != ' ':
            if _str[leftIdx] != _str[rightIdx]:
                return False
            else:
                leftIdx = leftIdx + 1
                rightIdx = rightIdx - 1
        elif _str[leftIdx] == ' ' and _str[rightIdx] == ' ':
            leftIdx = leftIdx - 1
            rightIdx = rightIdx - 1
        elif _str[leftIdx] == ' ':
            leftIdx = leftIdx + 1
        elif _str[rightIdx] == ' ':
            rightIdx = rightIdx - 1

    return True
    
class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(solution('eye'))
        self.assertTrue(solution2('eye'))
    def test_2(self):
        self.assertTrue(solution('noon'))
        self.assertTrue(solution2('noon'))
    def test_3(self):
        self.assertTrue(solution('decaf faced'))
        self.assertTrue(solution2('decaf faced'))
    def test_4(self):
        self.assertTrue(solution('taco cat'))
        self.assertTrue(solution2('taco cat'))
    def test_5(self):
        self.assertFalse(solution('racecars'))
        self.assertFalse(solution2('racecars'))
    def test_6(self):
        self.assertTrue(solution('borrow or rob'))
        self.assertTrue(solution2('borrow or rob'))
    def test_7(self):
        self.assertTrue(solution('  xx'))
        self.assertTrue(solution2('  xx'))

if __name__ == '__main__':
    unittest.main()
