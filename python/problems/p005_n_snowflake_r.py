def n_snowflake(n: int) -> int:
    return n_snowflake(n - 1) + 4 * (n - 1) if n > 1 else 1
