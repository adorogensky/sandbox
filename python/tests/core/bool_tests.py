#!/usr/bin/python3
import unittest

class PyBooleanTests(unittest.TestCase):
    def test_variable(self):
        input = True
        self.assertTrue(input)
    def test_type(self):
        self.assertEqual(bool, type(True))
    def test_isinstance(self):
        self.assertTrue(isinstance(True, bool))
    def test_true_and_true(self):
        self.assertTrue(True and True)
    def test_true_and_false(self):
        self.assertFalse(True and False)
    def test_true_or_true(self):
        self.assertTrue(True or True)
    def test_true_or_false(self):
        self.assertTrue(True or False)
    def test_not_true(self):
        self.assertFalse(not True)
    def test_not_false(self):
        self.assertTrue(not False)

if __name__ == '__main__':
    unittest.main()
