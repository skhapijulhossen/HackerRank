import calendar
days =['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
month, day, year = list(map(int, input().split()))
day = calendar.weekday(year, month, day)
print(days[day])