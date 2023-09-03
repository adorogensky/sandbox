#!/usr/bin/python3
import unittest

class PyTests(unittest.TestCase):
    def test_print(self):
        print("Hello World!")
        self.assertEqual(1, 1)
    def test_str_upper(self):
        self.assertEqual("HELLO", "hello".upper())

if __name__ == '__main__':
    unittest.main()
