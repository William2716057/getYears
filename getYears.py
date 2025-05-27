import calendar 
from datetime import date

weekDay = input("Enter weekday: ")
month_day = int(input("Enter day of month:  "))
#month, day = map(int, date.split())

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
    print("Invalid weekday entered.")
    exit()

# Find matching years
#matching_years = []
#matching_months = []

present = date.today().year
matches = []
for year in range(1900, present):
    try:
        for month in range(1, 13):
           if calendar.weekday(year, month, month_day) == target_day:
            #matching_years.append(year)
                dt = date(year, month, month_day)
                matches.append(dt.strftime("%A, %B %d, %Y"))
            #matching_months.append(month)
    except ValueError:
        continue

for match in matches:
    print(match)
# Print result
#print(f"\nYears when {month}/{weekDay} fell on a {weekDay.capitalize()}:")
#print(matching_years, matching_months)
#print(calendar.year(weekDay, date))
#for i in years 
#return years

#print(f"Years that {weekDay} fell on a {date}: {years}")
