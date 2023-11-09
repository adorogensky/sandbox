#!/usr/bin/python3
'''
Below we will define an n-interesting polygon.
Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim, side by side. 
You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
'''
import unittest

def solution(n):
    return 1 if n == 1 else solution(n - 1) + 4 * (n - 1)

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(1), 1)
    def test_2(self):
        self.assertEqual(solution(2), 5)
    def test_3(self):
        self.assertEqual(solution(3), 13)
    
if __name__ == '__main__':
    unittest.main()
