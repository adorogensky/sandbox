def n_snowflake(n: int) -> int:
    s, r = 0, 1
    for i in range(1, n):
        s += r
        r += 2
    return 2 * s + r
