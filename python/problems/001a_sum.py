'''
Calculate the sum of two numbers
'''
def sum(param1, param2):
    return param1 + param2

def test_0_0():
    assert sum(0, 0) == 0

def test_1_n1():
    assert sum(1, -1) == 0
