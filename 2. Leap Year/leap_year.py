def is_leap_year(year):
    if year<0 or year%1!=0:
        return False
    elif (year % 4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    
print(is_leap_year(2020))