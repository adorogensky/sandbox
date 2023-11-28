"""
In an array of numbers find max sequence of 1s
"""
def max_seq_1s(nums):
    ans = 0
    for i in range(len(nums)):
        if nums[i] != 1: continue
        c_ans = 0
        while i < len(nums) and nums[i] == 1:
            c_ans += 1
            i += 1
        ans = max(ans, c_ans)
    return ans

def test_01():
    assert max_seq_1s([]) == 0

def test_02():
    assert max_seq_1s([1]) == 1

def test_03():
    assert max_seq_1s([1, 1]) == 2

def test_04():
    assert max_seq_1s([0, 0]) == 0

def test_05():
    assert max_seq_1s([0, 0, 1]) == 1

def test_06():
    assert max_seq_1s([0, 0, 1, 2, 2, 1, 1, 1]) == 3
