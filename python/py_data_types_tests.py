#!/usr/bin/python3
import unittest
import math, sys

# bin
class PyDataTypesTests(unittest.TestCase):
    def test_boolean(self):
        self.assertEqual(bool, type(True))
        self.assertTrue(isinstance(True, bool))
        self.assertTrue(True and True)
        self.assertFalse(True and False)
        self.assertTrue(True or True)
        self.assertTrue(True or False)
        self.assertTrue(not False)
        self.assertFalse(not True)
    def test_integer(self):
        self.assertEqual(int, type(2))
        self.assertTrue(isinstance(2, int))
        self.assertEqual(4, 2 + 2)
        self.assertEqual(0, 2 - 2)
        self.assertEqual(6, 2 * 3)
        self.assertEqual(3.5, 7 / 2)
        self.assertEqual(3, 7 // 2)
        self.assertEqual(3, 7 % 4)
        self.assertEqual(8, 2 ** 3)
        self.assertTrue(3 > 2)
        self.assertTrue(3 >= 2)
        self.assertTrue(2 == 2)
        self.assertFalse(2 != 2)
        self.assertTrue(2 < 3)
        self.assertTrue(2 <= 2)
        self.assertEqual(0b10, 0b11 & 0b10)
        self.assertEqual(0b11, 0b11 | 0b10)
        self.assertEqual(0b01, 0b11 ^ 0b10)
        self.assertEqual(-6, ~0b101)
        self.assertEqual(-0b110, ~0b101)
        self.assertEqual(0b10, 0b1000 >> 2)
        self.assertEqual(0b1000, 0b10 << 2)
        self.assertEqual(2, int('2'))
        self.assertEqual(2, int('10', 2))
        self.assertEqual(15, int('F', 16))
        self.assertEqual(2, int(2.8))
        self.assertEqual(1, int(True))
        self.assertEqual(0, int(False))
    def test_float(self):
        self.assertEqual(float, type(2.0))
        self.assertTrue(isinstance(2.0, float))
        self.assertEqual(3.50, 3.5)
        self.assertEqual(1e-10, 0.0000000001)
        self.assertEqual(4.81, 1.22 + 3.59)
        self.assertTrue(2 < float('inf'))
        self.assertTrue(2 > float('-inf'))
        # self.assertEqual(1.331, 1.1 ** 3) # this doesnt work, real answer is 1.3310000000000004
        self.assertEqual(3.0, abs(-3.0))
        self.assertEqual(4, round(3.8))
        self.assertEqual(3, int(3.8))
        self.assertEqual(3, math.trunc(3.8))
        self.assertEqual(3.0, abs(-3.0))
        self.assertEqual(4, math.ceil(3.000001))
        self.assertEqual(3, math.floor(3.000001))
        # self.assertEqual(1.331, math.pow(1.1, 3)) # this doesnt work, real answer is 1.3310000000000004
        self.assertEqual(1.012345678901234, 1.012345678901234) 
        self.assertEqual(3.3333333333333335, 10 / 3)
        self.assertEqual(2.2360679774997896, math.sqrt(5)) # https://apod.nasa.gov/htmltest/gifcity/sqrt5.1mil
        self.assertEqual(1.213, math.fabs(-1.213))
        self.assertEqual(1.213, abs(-1.213))
        self.assertEqual(2, float(2))
        self.assertEqual(2.0, float(2.0))
        self.assertEqual(3.1, float('3.1'))
    def test_str(self):
        name = "Alex"
        self.assertEqual("Alex", name)
        self.assertEqual('Alex', "Alex")
        self.assertEqual('"Alex"', "\"Alex\"")
        self.assertEqual("'Alex'", '\'Alex\'')
        """
            Hello
            World
        """
        ''' 
            Hello
            World
        '''
        self.assertEqual(r'C:\Windows', 'C:\\Windows')
        self.assertTrue('Alex' == "Alex")
        self.assertTrue('alex' != 'Alex')
        self.assertTrue('a' < 'b')
        self.assertTrue('aa' < 'ab')
        self.assertTrue('A' < 'a')
        self.assertEqual('1', str(1))
        self.assertEqual('3.5', str(3.5))
        self.assertEqual('-1.0', str(-1.0))
        self.assertEqual('True', str(True))
        self.assertEqual('False', str(False))
        self.assertEqual('hi', ''.join(['h', 'i']))
    def test_list(self):
        self.assertEqual(['h', 'i'], list('hi'))
    def test_print_sys_float_info(self):    
        print(f'''
            {"digits".ljust(15)} = {sys.float_info.dig}        
            {"mantissa digits".ljust(15)} = {sys.float_info.mant_dig}
            {"max".ljust(15)} = {sys.float_info.max}
            {"min".ljust(15)} = {sys.float_info.min}
            {"max 2 exp".ljust(15)} = {sys.float_info.max_exp}
            {"min 2 exp".ljust(15)} = {sys.float_info.min_exp}
            {"max 10 exp".ljust(15)} = {sys.float_info.max_10_exp}
            {"min 10 exp".ljust(15)} = {sys.float_info.min_10_exp}
        ''')
    

if __name__ == '__main__':
    unittest.main()

