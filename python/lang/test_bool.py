def test_var():
    i = True
    assert i == True

def test_type():
    assert type(True) == bool
    assert type(False) == bool

def test_isinstance():
    assert isinstance(True, bool) == True
    assert isinstance(False, bool) == True

def test_and_true_true():
    assert (True and True) == True

def test_and_true_false():
    assert (True and False) == False

def test_and_false_false():
    assert (False and False) == False

def test_or_true_true():
    assert (True or True) == True

def test_or_true_false():
    assert (True or False) == True

def test_or_false_false():
    assert (False or False) == False
    
def test_not_true():
    assert (not True) == False

def test_not_false():
    assert (not False) == True

def test_int_equal():
    assert 2 == 2

def test_int_not_equal(): 
    assert (2 != 2) == False

def test_int_greater():     
    assert (3 > 2) == True

def test_int_greater_equal():
    assert (3 >= 2) == True

def test_int_less():
    assert (2 < 3) == True

def test_int_less_equal():
    assert (2 <= 2) == True
