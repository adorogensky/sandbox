#!/usr/bin/python3
'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be bigger than
the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''
import unittest

def solution(arr):
    arr.sort()
    n = 0
    for i in range(0, len(arr) - 1):
        n = n + arr[i + 1] - arr[i] - 1

    return n

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([6, 2, 3, 8]), 3)
    def test_2(self):
        self.assertEqual(solution([0, 3]), 2)
    def test_3(self):
        self.assertEqual(solution([5, 4, 6]), 0)

if __name__ == '__main__':
    unittest.main()

