#!/usr/bin/python3
import unittest

class PyTests(unittest.TestCase):
    def test2(self):
        print("Hello World!\n")
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
