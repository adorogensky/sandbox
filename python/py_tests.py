#!/usr/bin/python3
import unittest

class PyTests(unittest.TestCase):
    def test_var(self):
        name = "Alex"
        self.assertEqual("Alex", name)
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
    def test_list_remove(self):
        names = ["John", "Mike"]
        remove_return = names.remove('John')
        self.assertEqual(None, remove_return)
        self.assertEqual(["Mike"], names)

if __name__ == '__main__':
    unittest.main()
