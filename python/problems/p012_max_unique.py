from typing import List

def max_unique(a: List[int]) -> int:
    a.sort()
    i = len(a) - 1
    while i >= 0:
        if i == 0 or a[i] != a[i - 1]:
            return a[i]
        while i > 0 and a[i] == a[i - 1]:
            i -= 1
        i -= 1
    return -1
