#!/usr/bin/python3
import unittest
import math, sys

# bin
class PyFloatTests(unittest.TestCase):
    def test_variable(self):
        x = 2.3
        self.assertEqual(x, 2.3)
    def test_type(self):
        self.assertEqual(float, type(2.0))
    def test_isinstance(self):
        self.assertTrue(isinstance(2.0, float))
    def test_trailing_float_zeros(self): 
        self.assertEqual(3.50, 3.5)
    def test_max_fraction_digits(self):
        # not sure how many fraction digits does a float represents, maybe 16?
        self.assertEqual(1.12345678901234567890, 1.12345678901234567890) 
    def test_scientific_notation(self):
        self.assertEqual(1e-10, 0.0000000001)
    def test_add(self):
        self.assertEqual(4.81, 1.22 + 3.59)
    def test_negative_infinity(self):
        self.assertTrue(2 > float('-inf'))
    def test_postive_infinity_1(self):
        self.assertTrue(2 < float('inf'))
    def test_postive_infinity_2(self):
        self.assertTrue(float('-inf') < float('inf'))
        # self.assertEqual(1.331, 1.1 ** 3) # this doesnt work, real answer is 1.3310000000000004
    def test_abs(self):
        self.assertEqual(3.0, abs(-3.0))
    def test_round(self):
        self.assertEqual(4, round(3.8))
    def test_to_int(self):
        self.assertEqual(3, int(3.8))
    def test_math_trunc(self):
        self.assertEqual(3, math.trunc(3.8))
    def test_math_ceil(self):
        self.assertEqual(4, math.ceil(3.000001))
    def test_math_floor(self):
        self.assertEqual(3, math.floor(3.000001))
    def test_divide(self):
        self.assertEqual(3.3333333333333335, 10 / 3)
    def test_math_sqrt(self):
        self.assertEqual(2.2360679774997896, math.sqrt(5)) # https://apod.nasa.gov/htmltest/gifcity/sqrt5.1mil
    def test_math_fabs_vs_abs(self):
        self.assertEqual(1.213, math.fabs(-1.213))
        self.assertEqual(1.213, abs(-1.213))
    def test_int_to_float_int(self):
        self.assertEqual(2, float(2))
    def test_float_to_float(self):
        self.assertEqual(2.0, float(2.0))

if __name__ == '__main__':
    unittest.main()
