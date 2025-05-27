
import calendar 

weekDay = input("Enter weekday: ")
date = input("Enter day of month: ")
month, day = map(int, date.split())

weekday_map = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
    }

target_day = weekday_map.get(weekDay)

matching_years = []
for year in range(1900, 2101):
    try:
        if calendar.weekday(year, month, day) == target_day:
            matching_years.append(year)
    except ValueError:
        continue
    print(matching_years)
#print(calendar.year(weekDay, date))
#for i in years 
#return years

#print(f"Years that {weekDay} fell on a {date}: {years}")
