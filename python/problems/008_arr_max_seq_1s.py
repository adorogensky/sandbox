def find_max_ones_seq(nums):
    g_ans = 0
    for i in range(len(nums)):
        if nums[i] != 1: continue
        l_ans = 0
        while i < len(nums) and nums[i] == 1:
            l_ans += 1
            i += 1
        g_ans = max(g_ans, l_ans)
    return g_ans

def test_01():
    assert find_max_ones_seq([]) == 0

def test_02():
    assert find_max_ones_seq([1]) == 1

def test_03():
    assert find_max_ones_seq([1, 1]) == 2

def test_04():
    assert find_max_ones_seq([0, 0]) == 0

def test_05():
    assert find_max_ones_seq([0, 0, 1]) == 1

def test_06():
    assert find_max_ones_seq([0, 0, 1, 2, 2, 1, 1, 1]) == 3
