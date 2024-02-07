import datetime as dt

total_sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if dt.date(year, month, 1).weekday() == 6:
            total_sundays += 1

print("Solution is: " + str(total_sundays))
