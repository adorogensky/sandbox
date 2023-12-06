#!/usr/bin/python3
import unittest
'''
Write a function that returns the sum of two numbers
Example:
    For param1 = 1 and param2 = 2, the output should be
    solution(param1, param2) = 3
'''

def solution(param1, param2):
    return param1 + param2

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()

