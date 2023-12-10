def factorial(n: int) -> int:
    return n * factorial(n - 1) if n > 0 else 1
