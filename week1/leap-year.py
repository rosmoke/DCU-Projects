year = 2016
is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print year, "is a leap year:", is_leap_year