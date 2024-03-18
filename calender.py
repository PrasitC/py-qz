import datetime
import random

def find_day(date):
    day_number = date.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day_number]


def generate_random_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    
    day = random.randint(1, 28) 
    return datetime.datetime(year, month, day)


start_year = 2000
end_year = 2030

random_date = generate_random_date(start_year, end_year)


print("Randomly generated date:", random_date.strftime("%Y-%m-%d"))

year = random_date.year
month = random_date.month
day = random_date.day
print("Step 1: Year:", year, ", Month:", month, ", Day:", day)


if month < 3:
    month += 12
    year -= 1


K = year % 100
J = year // 100


h = (day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7


days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day_of_week_zeller = days[h]



print("Step 2: Zeller's Congruence Algorithm")
print("   K (last two digits of the year):", K)
print("   J (first two digits of the year):", J)
print("   h (the special number we found):", h)
print("Step 3: Calculated day of the week using Zeller's Congruence algorithm:", day_of_week_zeller)

day_of_week_using_weekday = find_day(random_date)
print("Step 4: Day of the week using weekday() function:", day_of_week_using_weekday)