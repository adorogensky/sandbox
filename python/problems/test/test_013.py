'''
 find number of days in a month on a given year
'''
from p013_month_days import month_days

def test_01():
    assert month_days(2000, 1) == 31

def test_02():
    assert month_days(2000, 2) == 29

def test_03():
    assert month_days(2001, 2) == 28

def test_04():
    assert month_days(2001, 3) == 31

def test_05():
    assert month_days(2001, 4) == 30

def test_06():
    assert month_days(2001, 5) == 31

def test_07():
    assert month_days(2001, 6) == 30

def test_08():
    assert month_days(2001, 7) == 31

def test_09():
    assert month_days(2001, 8) == 31

def test_10():
    assert month_days(2001, 9) == 30

def test_11():
    assert month_days(2000, 9) == 30

def test_12():
    assert month_days(2000, 10) == 31

def test_13():
    assert month_days(2000, 11) == 30

def test_14():
    assert month_days(2000, 12) == 31
