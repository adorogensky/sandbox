#!/usr/bin/python3
import unittest

# unsupported list operations: -, * (when the right operand is not an integer) 

class PyListTests(unittest.TestCase):
    def test_list_len(self):
        self.assertEqual(2, len([0, 0]))
    def test_list_access_element(self):
        list = [5, 3, 2]
        self.assertEqual(3, list[1])
        self.assertEqual(2, list[-1])
    def test_list_slice(self):
        list = [4, 1, 2, 5, 7]
        self.assertEqual(list, list[:])
        self.assertEqual([1, 2, 5, 7], list[1:])
        self.assertEqual([4, 1, 2], list[:3])
        self.assertEqual([1, 2, 5], list[1:4])
        self.assertEqual([1, 2, 5], list[1:-1])
    def test_list_concat(self):
        self.assertEqual([1, 2, 3, 4], [1, 2] + [3, 4])
    def test_list_multiply(self):
        self.assertEqual([1, 1, 1], [1] * 3)
    def test_list_in(self):
        self.assertTrue(2 in [1, 2, 3])
    def test_list_copy(self):
        self.assertEqual([1, 2, 3], [1, 2, 3].copy())
    def test_list_enumerate(self):
        str = []
        for index, value in enumerate([10, 20, 30]):
            str = str + list(f"[{index}] = {value}\n") 
        self.assertEqual("[0] = 10\n[1] = 20\n[2] = 30\n", ''.join(str))    
    def test_list_append(self):
        names = ["John", "Mike"]
        append_return = names.append("James")
        self.assertEqual(["John", "Mike", "James"], names)
        self.assertEqual(None, append_return)
    def test_list_insert(self):
        list = [1, 3]
        list.insert(1, 2)
        self.assertEqual([1, 2, 3], list)
    def test_list_del(self):
        names = ["John", "Mike"]
        del names[0] # doesnt return anything 
        self.assertEqual(["Mike"], names)
    def test_list_remove(self):
        names = ["John", "Mike"]
        remove_return = names.remove('John')
        self.assertEqual(None, remove_return)
        self.assertEqual(["Mike"], names)
    def test_list_pop(self):
        names = ["John", "Mike"]
        pop_return = names.pop()
        self.assertEqual('Mike', pop_return)
        self.assertEqual(["John"], names)
    def test_list_clear(self):
        list = [1, 2]
        list.clear()
        self.assertEqual([], list)
    def test_list_comprehensions(self):
        self.assertEqual([1, 4, 9], [x**2 for x in [1, 2, 3]])
    def test_list_index(self):
        self.assertEqual(1, [1, 5, 9].index(5))
    def test_sort(self):
        list = [5, 2, 3]
        list.sort()
        self.assertEqual([2, 3, 5], list)
    def test_sorted(self):   
        list = [5, 2, 3]
        sorted_list = sorted(list)
        self.assertEqual([5, 2, 3], list)
        self.assertEqual([2, 3, 5], sorted_list) 
    def test_list_reverse(self):
        list = [3, 2, 1]
        list.reverse()
        self.assertEqual([1, 2, 3], list)

if __name__ == '__main__':
    unittest.main()
