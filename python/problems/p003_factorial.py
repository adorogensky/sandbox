def factorial(n: int) -> int:
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
