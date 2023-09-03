#!/usr/bin/python3
import unittest

class PyTests(unittest.TestCase):
    def test_print(self):
        print("Hello World!")
        self.assertEqual(1, 1)
    def test_str_upper(self):
        self.assertEqual("HELLO", "hello".upper())
    def test_str_lower(self):
        self.assertEqual("hello", "HEllo".lower())
    def test_str_concat(self):
        self.assertEqual("Hello" + " World!", "Hello World!")
    def test_str_f_str(self):
        name = "Alex"
        self.assertEqual(f"Hello {name}", "Hello Alex")
    def test_list_append(self):
        names = ["John", "Mike"]
        append_return = names.append("James")
        self.assertEqual(["John", "Mike", "James"], names)
        self.assertEqual(None, append_return)
    def test_list_del(self):
        names = ["John", "Mike"]
        del names[0] # wont return None
        self.assertEqual(["Mike"], names)

if __name__ == '__main__':
    unittest.main()
