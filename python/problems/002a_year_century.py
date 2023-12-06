#!/usr/bin/python3
import unittest

'''
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.

Example:
    For year = 1905, the output should be solution(year) = 20
    For year = 1700, the output should be solution(year) = 17
'''

#   1 - 100 is 1st century
# 101 - 200 is 2nd century
# 201 - 300 is 3rd century
def solution(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(1905), 20)
    def test_2(self):
        self.assertEqual(solution(1700), 17)

if __name__ == '__main__':
    unittest.main()
