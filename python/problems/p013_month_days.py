def _is_leap_year(year: int) -> int:
    if year % 4 != 0: return False
    if year % 100 != 0: return True
    return True if year % 400 == 0 else False

def _month_days(year: int, month: int, b4_aug: bool) -> int:
    if month > 7:
        return _month_days(year, month - 7, b4_aug)
    if month % 2 == 0:
        if month == 2 and b4_aug:
            return 29 if _is_leap_year(year) else 28
        else:
            return 30
    else:
        return 31

def month_days(year: int, month: int) -> int:
    return _month_days(year, month, month < 8) if month > 0 and month < 13 else None
