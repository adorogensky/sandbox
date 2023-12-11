def _is_leap_year(year: int) -> int:
    if year % 4 != 0: return False
    if year % 100 != 0: return True
    return True if year % 400 == 0 else False

def month_days(year: int, month: int) -> int:
    if month < 1 or month > 12 or year < 1: return None
    seq = month - 7 if month > 7 else month
    if month == 2: return 29 if _is_leap_year(year) else 28
    return 31 if seq % 2 == 1 else 30
