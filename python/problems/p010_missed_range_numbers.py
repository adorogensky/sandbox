def missed_range_numbers(a) -> int:
    a.sort()
    n = 0
    for i in range(0, len(a) - 1):
        n += a[i + 1] - a[i] - 1
    return n
