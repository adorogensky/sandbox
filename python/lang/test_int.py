def test_var():
    input = 1
    assert input == 1

def test_var_from_str():    
    assert int('2') == 2

def test_var_from_str_bin():
    assert int('10', 2) == 2

def test_var_from_str_hex():
    assert int('F', 16) == 15

def test_var_from_float():
    assert int(2.8) == 2

def test_var_from_true():
    assert int(True) == 1

def test_var_from_false():
    assert int(False) == 0

def test_type():
    assert type(1) == int

def test_isinstance():
    assert isinstance(2, int) == True

def test_add():   
    assert 2 + 2 == 4

def test_subtract():
    assert 2 - 2 == 0

def test_multiply():    
    assert 2 * 3 == 6

def test_power():
    assert 2 ** 3 == 8

def test_float_divide():
    assert 3 / 2 == 1.5

def test_int_divide():
    assert 3 // 2 == 1

def test_modulus():   
    assert 7 % 4 == 3

def test_bitwise_and():
    assert (0b11 & 0b10) == 0b10

def test_bitwise_or():
    assert (0b11 | 0b10) == 0b11

def test_bitwise_exclusive_or():
    assert (0b11 ^ 0b10) == 0b01

def test_bitwise_complement_2():
    assert ~0b101 == -0b110 # -6

def test_bitwise_right_shift():
    assert 0b1000 >> 2 == 0b10

def test_bitwise_left_shift():
    assert 0b10 << 2 == 0b1000

