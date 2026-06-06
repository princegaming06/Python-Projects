import time
import calendar

def is_leap_year(year):
    if calendar.isleap(year):
        return 366
    else:
        return 365

# Import Local Time
local_time = time.localtime()

# importing date time and year from local_time
current_year = local_time.tm_year
current_date = local_time.tm_mday
current_month = local_time.tm_mon 
monthInYear = 12
# Input User Age.
while True:
    try:
        user_yob = int(input("Enter Your birth year: "))
        user_mob = int(input("Enter Your birth month: "))
        user_dob = int(input("Enter Your birth date: "))
        
        # Year validation
        if not (1900 <= user_yob <= current_year):
            print("Invalid year!")
            continue
        # Month Validation
        if not (1 <= user_mob <= 12):
            print("invalid month!")
            continue
        # Max number of day in a month
        max_days = calendar.monthrange(user_yob, user_mob)[1]
        # Date validation
        if not (1 <= user_dob <= max_days):
            print(f"error? day {user_dob} is not in month {user_mob} of year {user_yob}..!")
            continue
        # break when all right
        break
    except ValueError:
        print("You Enters Wrong Age..!")

print(f"{user_dob}-{user_mob}-{user_yob}")

# months in year of born
month_yob = monthInYear - user_mob 

# Count Age 
age = current_year - (user_yob + 1)
age_months = month_yob + current_month
age_days = user_dob + current_date
## Month Count
# 12 - user_mob + 12*18
month_in_age = monthInYear * age

total_month = month_yob + month_in_age + current_month



# Day count in mob 
day_count_mob = user_dob

#Day in user_yob
day_count_yob = 0
for month in range(user_mob + 1, monthInYear + 1):
    day_count_yob += calendar.monthrange(user_yob, month)[1]

#Days for months in user_yob to current year
day_count_age = 0 
for year in range(user_yob + 1, current_year):
    for month in range(1, monthInYear + 1):
        day_count_age += calendar.monthrange(year, month)[1]

# Days in current year
day_count_currentYear = 0
for month in range(1, current_month):
    day_count_currentYear += calendar.monthrange(current_year, month)[1]

# Days in currennt month
day_count_currentMonth = current_date


# Day Count ==> Days in month of born + days in year of born + Days in user_yob to current year (not counting both) + Days in current year + Days in current month.

day_count = day_count_mob + day_count_yob + day_count_age + day_count_currentYear + day_count_currentMonth

print (f"Your age: {age} Years {age_months} Months and {age_days} Days or {total_month} Months {age_days} Days or {day_count} Days")