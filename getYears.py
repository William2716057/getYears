import calendar 
from datetime import date

weekDay = input("Enter weekday: ")
month_day = int(input("Enter day of month:  "))
# Map weekday name to number
weekday_map = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}
# Get numeric weekday
target_day = weekday_map.get(weekDay)
if target_day is None:
    print("Invalid weekday.")
    exit()

present = date.today().year
matches = []
for year in range(1900, present):
    try:
        for month in range(1, 13):
           if calendar.weekday(year, month, month_day) == target_day:

                dt = date(year, month, month_day)
                matches.append(dt.strftime("%A, %B %d, %Y"))
    except ValueError:
        continue

for match in matches:
    print(match)
