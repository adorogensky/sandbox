#!/usr/bin/python3
import unittest
import math, sys

class PyDataTypesTests(unittest.TestCase):
    def test_variable(self):
        input = 3
        self.assertEqual(3, input)
    def test_type(self):
        self.assertEqual(int, type(2))
    def test_isinstance(self):
        self.assertTrue(isinstance(2, int))
    def test_add(self):   
        self.assertEqual(4, 2 + 2)
    def test_subtract(self):
        self.assertEqual(0, 2 - 2)
    def test_multiply(self):    
        self.assertEqual(6, 2 * 3)
    def test_float_divide(self):
        self.assertEqual(3.5, 7 / 2)
    def test_integer_divide(self):
        self.assertEqual(3, 7 // 2)
    def test_modulus(self):   
        self.assertEqual(3, 7 % 4)
    def test_power(self):
        self.assertEqual(8, 2 ** 3)
    def test_greater(self):     
        self.assertTrue(3 > 2)
    def test_greater_or_equal(self):
        self.assertTrue(3 >= 2)
    def test_equal(self):
        self.assertTrue(2 == 2)
    def test_not_equal(self): 
        self.assertFalse(2 != 2)
    def test_less(self):
        self.assertTrue(2 < 3)
    def test_less_or_equal(self):
        self.assertTrue(2 <= 2)
    def test_bitwise_and(self):
        self.assertEqual(0b10, 0b11 & 0b10)
    def test_bitwise_or(self):
        self.assertEqual(0b11, 0b11 | 0b10)
    def test_bitwise_exclusive_or(self):
        self.assertEqual(0b01, 0b11 ^ 0b10)
    def test_bitwise_complement_1(self):
        self.assertEqual(-6, ~0b101)
    def test_bitwise_complement_2(self):
        self.assertEqual(-0b110, ~0b101)
    def test_bitwise_right_shift(self):
        self.assertEqual(0b10, 0b1000 >> 2)
    def test_bitwise_left_shift(self):
        self.assertEqual(0b1000, 0b10 << 2)
    def test_from_string(self):    
        self.assertEqual(2, int('2'))
    def test_from_string_base_2(self):
        self.assertEqual(2, int('10', 2))
    def test_from_string_base_16(self):
        self.assertEqual(15, int('F', 16))
    def test_from_float(self):
        self.assertEqual(2, int(2.8))
    def test_from_true(self):
        self.assertEqual(1, int(True))
    def test_from_false(self):
        self.assertEqual(0, int(False))

if __name__ == '__main__':
    unittest.main()
