def _is_leap_year(year: int) -> int:
    if year % 4 != 0: return False
    if year % 100 != 0: return True
    return True if year % 400 == 0 else False

def _month_days(year: int, month: int, is_jan_jul: bool) -> int:
    if month > 7:
        return _month_days(year, month - 7, is_jan_jul)
    if month % 2 == 1: return 31
    if month == 2 and is_jan_jul: return 29 if _is_leap_year(year) else 28
    return 30

def month_days(year: int, month: int) -> int:
    return _month_days(year, month, month < 8) if month > 0 and month < 13 else None
