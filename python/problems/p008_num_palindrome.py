def is_palindrome(n: int) -> bool:
    digits = [] 
    while n > 0:
        digits.append(n if n < 10 else n % 10)
        n //= 10
    for i in range(0, len(digits) // 2):
        if digits[i] != digits[len(digits) - 1 - i]:
            return False
    return True
