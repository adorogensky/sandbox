from typing import List

def max_1s_seq(a: List[int]) -> int:
    c = 0
    for i in range(len(a)):
        if a[i] == 1:
            c2 = 0
            while i < len(a) and a[i] == 1:
                c2 += 1
                i += 1
            c = max(c, c2)
    return c
