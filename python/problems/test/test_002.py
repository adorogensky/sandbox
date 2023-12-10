'''
find year's century
e.g.
    years   1 - 100 is 1st century
    years 101 - 200 is 2nd century
    years 201 - 300 is 3rd century
    year 1700 - is 17th century
    year 1905 - is 20st century
'''
from p002_year_century import year_century

def test_1():
    assert year_century(1) == 1

def test_100():
    assert year_century(100) == 1

def test_101():
    assert year_century(101) == 2

def test_1905():
    assert year_century(1905) == 20

def test_1700():
    assert year_century(1700) == 17
