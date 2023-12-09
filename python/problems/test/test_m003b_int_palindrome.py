'''
find if an integer is a palindrome,
e.g.

   1 is a palindrome
  12 is NOT a palindrome
  22 is a palindrome
 212 is a palindrome
'''
from m003b_int_palindrome import is_palindrome

def test_1():
    assert is_palindrome(1) == True

def test_12():
    assert is_palindrome(12) == False

def test_22():
    assert is_palindrome(22)

def test_212():
    assert is_palindrome(212)
