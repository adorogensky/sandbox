#!/usr/bin/python3
import unittest

# 1. why not define len() on String -- to be consistent with global len()
# 2. "hello"[0] = 'H' is illegal -- because string objects are immutable

# format, replace, split, rsplit, count, truncate 
# startswith, endswith, isalpha, isdigit, isalnum, isascii, isspace
# islower, isupper, isnumeric, isdecimal, isprintable 
# rjust, ljust, center, zfill
class PyStrTests(unittest.TestCase):
    def test_str_len(self):
        self.assertEqual(5, len("hello"))    
    def test_str_char_at(self):
        self.assertEqual('h', "hello"[0])
        self.assertEqual('o', "hello"[-1]) 
    def test_str_sub_str(self):
        self.assertEqual("hello", "hello"[0:])
        self.assertEqual("", "hello"[:0])
        self.assertEqual("el", "hello"[1:3])
        self.assertEqual("ll", "hello"[-3:-1])
        self.assertEqual("lo", "hello"[-2:])
    def test_str_concat(self):
        self.assertEqual("Hello" + " World!", "Hello World!")
    def test_str_f_str(self):
        name = "Alex"
        self.assertEqual(f"Hello {name}", "Hello Alex")
    def test_str_find(self):
        self.assertEqual(2, 'hello'.find('l'))
        self.assertEqual(3, 'hello'.find('l', 3))
        self.assertEqual(-1, 'hello'.find('H'))
    def test_str_index(self):
        self.assertEqual(2, 'hello'.index('l'))
        self.assertEqual(3, 'hello'.index('l', 3))
        with self.assertRaises(ValueError):
            'hello'.index('H')
    def test_str_title(self):
        self.assertEqual("Hello World", "hello world".title())
    def test_str_capitalize(self):
        self.assertEqual("Hello world", "hello world".capitalize())
    def test_str_upper(self):
        self.assertEqual("HELLO", "hello".upper())
    def test_str_lower(self):
        self.assertEqual("hello", "HEllo".lower())

if __name__ == '__main__':
    unittest.main()
