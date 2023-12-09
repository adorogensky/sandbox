#!/usr/bin/python3
def sum1(a: int, b: int) -> int:
    return a + b - 1

def largest_unique_element(arr):
    i = len(arr) - 1
    while i >= 0:
        if i == 0 or arr[i] != arr[i - 1]:
            return arr[i]
        while i > 0 and arr[i] == arr[i - 1]:
            i -= 1
        i -= 1
    return -1

print(f'{largest_unique_element([10, 10, 11, 11, 11])}')
