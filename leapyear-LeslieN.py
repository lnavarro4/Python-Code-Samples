
#Leslie N
#3/08/25

#Problem 4
#Check if year is leap year

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
        return True
    else:
        return False


