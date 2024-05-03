def leap_year(year):
    return True if year % 100 == 0 and year % 400 == 0 else year % 4 == 0 and not year % 100 == 0