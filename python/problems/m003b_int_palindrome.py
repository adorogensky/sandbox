def is_palindrome(_int):
    if _int < 10:
        return True
   
    _int_digits = []
    _int_digits.append(_int % 10)
    _int = _int // 10

    while True:
        if _int < 10:
            _int_digits.append(_int)
            break
        else:
            _int_digits.append(_int % 10)
            _int = _int // 10

    _int_digits_len = len(_int_digits)
    for i in range(0, _int_digits_len // 2):
        if _int_digits[i] != _int_digits[_int_digits_len - 1 - i]:
            return False
    
    return True
