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
    def test_str_char_at_positive_idx(self):
        self.assertEqual('h', "hello"[0])
    def test_str_char_at_negative_idx(self):
        self.assertEqual('o', "hello"[-1]) 
    def test_str_slice_positive_start_idx(self):
        self.assertEqual("hello", "hello"[0:])
    def test_str_slice_positive_end_idx(self):
        self.assertEqual("", "hello"[:0])
    def test_str_slice_positive_start_and_end_idx(self):
        self.assertEqual("el", "hello"[1:3])
    def test_str_slice_negative_start_and_end_idx(self):
        self.assertEqual("ll", "hello"[-3:-1])
    def test_str_slice_negative_end_idx(self):
        self.assertEqual("lo", "hello"[-2:])
    def test_str_concat(self):
        self.assertEqual("Hello" + " World!", "Hello World!")
    def test_f_str(self):
        name = "Alex"
        self.assertEqual(f"Hello {name}", "Hello Alex")
    def test_str_find_when_findable(self):
        self.assertEqual(2, 'hello'.find('l'))
    def test_str_find_when_findable_starting_idx(self):
        self.assertEqual(3, 'hello'.find('l', 3))
    def test_str_find_when_not_findable(self):
        self.assertEqual(-1, 'hello'.find('H'))
    def test_str_index_when_findable(self):
        self.assertEqual(2, 'hello'.index('l'))
    def test_str_index_when_findable_starting_idx(self):
        self.assertEqual(3, 'hello'.index('l', 3))
    def test_str_index_when_not_findable(self):
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
