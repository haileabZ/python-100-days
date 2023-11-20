def isleap(year):
    if (year % 400 == 0) or  ((year % 100 != 0) and  (year % 4 == 0)):
        return True
    else:
        return False
def day_finder(year,month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        days[1]=29
    print("number of days: ",days[month-1])

month=int(input("enter the month:"))
year=int(input("enter the year:"))
day_finder(year,month)
