import unittest

def greater_than_zero(num):
    if (num > 0):
        return 'greater than zero'
    elif (num == 0):
        return 'equal to zero'
    else:
        return 'less than zero'

def greater_than_zero2(num):
    return 'greater than zero' if (num > 0) else ('equal to zero' if num == 0 else 'less than zero')

class PyControlLogicTests(unittest.TestCase):
    def test_if(self):
        self.assertEqual('greater than zero', greater_than_zero(1))
        self.assertEqual('equal to zero', greater_than_zero(0))
        self.assertEqual('less than zero', greater_than_zero(-1))
    def test_tertiary(self):
        self.assertEqual('greater than zero', greater_than_zero2(1))
        self.assertEqual('equal to zero', greater_than_zero2(0))
        self.assertEqual('less than zero', greater_than_zero2(-1))
    def test_for_lists(self):
        arr = [1, 2, 3]
        sum = 0
        for i in arr:
            sum += i 
        self.assertEqual(6, sum)
    def test_for_str(self):
        str_letters = []
        for letter in 'hi':
            str_letters.append(letter)
        self.assertEqual(['h', 'i'], str_letters)    
    def test_for_list_range(self):
        arr = [1, 2, 3]
        str_arr = []
        for i in range(0, len(arr)):
            str_arr.append(str(arr[i]))
        self.assertEqual('123', ''.join(str_arr))    
    def test_for_list_step_range(self):
        arr = [1, 2, 3]
        str_arr = []
        for i in range(0, len(arr), 2):
            str_arr.append(str(arr[i]))
        self.assertEqual('13', ''.join(str_arr))    
    def test_for_list_enumerate(self):
        arr = [1, 2, 3]
        product = 0
        for i, el in enumerate(arr):
            product += i * el
        self.assertEqual(8, product)
    def test_for_list_break(self):
        arr = [7, 9, 22]
        idx = -1

        for i, el in enumerate(arr):
            if el == 22:
                idx = i
                break

        self.assertEqual(2, idx)
    def test_for_list_continue(self):
        arr = [1, 2, 5, 6, 8]
        sum = 0
        for i in arr:
            if i % 2 == 0:
                continue
            sum += i
        self.assertEqual(6, sum)
if __name__ == '__main__':
    unittest.main()
