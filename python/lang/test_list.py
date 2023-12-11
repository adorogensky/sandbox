#!/usr/bin/python3
import unittest

# unsupported list operations: -, * (when the right operand is not an integer) 

arr = [1, 2, 3, 4, 5]

class PyListTests(unittest.TestCase):
    def test_len(self):
        self.assertEqual(5, len(arr))
    def test_element_at_positive_idx(self):
        self.assertEqual(4, arr[3])
    def test_element_at_negative_idx(self):
        self.assertEqual(5, arr[-1])
    def test_slice_right_open_range(self):
        self.assertEqual([2, 3, 4, 5], arr[1:])
    def test_slice_left_open_range(self):
        self.assertEqual([1, 2, 3], arr[:3])
    def test_slice_close_range(self):
        self.assertEqual([2, 3, 4], arr[1:4])
    def test_slice_close_range_negative_right_idx(self):
        self.assertEqual([2, 3, 4], arr[1:-1])
    def test_slice_close_range_negative_left_idx(self):
        self.assertEqual([4, 5], arr[-2:5])
    def test_slice_close_range_negative_left_and_right_idx(self):
        self.assertEqual([4], arr[-2:-1])
    def test_slice_copy(self):
        self.assertEqual(arr, arr[:])
        self.assertFalse(arr is arr[:])
    def test_concat(self):
        self.assertEqual([1, 2, 3, 4], [1, 2] + [3, 4])
    def test_multiple_1_element_list_by_int(self):
        self.assertEqual([1, 1, 1], [1] * 3)
    def test_multiple_1_element_list_by_int(self):
        self.assertEqual([1, 1, 1, 1, 1, 1], [1, 1] * 3)
    def test_in(self):
        self.assertTrue(2 in [1, 2, 3])
    def test_copy(self):
        self.assertEqual([1, 2, 3], [1, 2, 3].copy())
    def test_append(self):
        names = ["John", "Mike"]
        append_return = names.append("James")
        self.assertEqual(["John", "Mike", "James"], names)
        self.assertEqual(None, append_return)
    def test_insert(self):
        arr2 = [1, 2, 3]
        arr2.insert(1, 2)
        self.assertEqual([1, 2, 2, 3], arr2)
    def test_del(self):
        names = ["John", "Mike"]
        del names[0] # doesnt return anything 
        self.assertEqual(["Mike"], names)
    def test_remove(self):
        names = ["John", "Mike"]
        remove_return = names.remove('John')
        self.assertEqual(None, remove_return)
        self.assertEqual(["Mike"], names)
    def test_pop(self):
        names = ["John", "Mike"]
        pop_return = names.pop()
        self.assertEqual('Mike', pop_return)
        self.assertEqual(["John"], names)
    def test_clear(self):
        arr2 = [1, 2, 3]
        arr2.clear()
        self.assertEqual([], arr2)
    def test_comprehensions(self):
        self.assertEqual([1, 4, 9], [x**2 for x in [1, 2, 3]])
    def test_index(self):
        self.assertEqual(1, [1, 5, 9].index(5))
    def test_sort(self):
        arr2 = [5, 2, 3]
        arr2.sort()
        self.assertEqual([2, 3, 5], arr2)
    def test_sorted(self):   
        arr2 = [5, 2, 3]
        sorted_list = sorted(arr2)
        self.assertEqual([5, 2, 3], arr2)
        self.assertEqual([2, 3, 5], sorted_list) 
    def test_reverse(self):
        arr2 = [3, 2, 1]
        arr2.reverse()
        self.assertEqual([1, 2, 3], arr2)
    def test_for_enumerate(self):
        s = 0
        for index, value in enumerate([10, 20, 30]):
            s += (index + value)
        self.assertEqual(s, 63)

if __name__ == '__main__':
    unittest.main()
