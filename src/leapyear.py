

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # ekstra regel som eliminerer år delbare på 4000.
        if year % 4000 == 0:
            return False

        return True
    else:
        return False
    return year
