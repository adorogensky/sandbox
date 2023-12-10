'''
find if str is a palindrome, i.e. when it reads the same backward and forward (excluding spaces)
e.g.
  "eye" is a palindrome
  "noon" is a palindrome
  "taco cat" is a palindrome 
  "race cars" is not a palindrome
  "borrow or rob" is a palindrome
'''
from p007_str_palindrome import is_palindrome

def test_eye():
    assert is_palindrome('eye') == True

def test_bye():
    assert is_palindrome('bye') == False

def test_noon():
    assert is_palindrome('noon') == True

def test_name():
    assert is_palindrome('name') == False

def test_taco_cat():
    assert is_palindrome('taco cat') == True

def test_race_cars():
    assert is_palindrome('race cars') == False

def test_borrow_or_rob():
    assert is_palindrome('borrow or rob') == True

def test_xx():
    assert is_palindrome('  xx') == True
