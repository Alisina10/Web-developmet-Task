import datetime
from datetime import datetime, timedelta

#lab 1

now = datetime.now()
format_now = now.strftime('%Y-%m-%d %H:%M:%S')
print("Current datetime is", format_now)

#lab 2
today = datetime.now()
new_year = datetime(today.year, 3, 1)

if today > new_year:
    new_year = datetime(today.year + 1, 12, 31)

days_to_new_year = (new_year - today).days
print(days_to_new_year)

#lab 3

def countdown_timer(seconds):
    endtime = datetime.now() + timedelta(seconds=seconds)

    while True:
        remaining = (endtime - datetime.now()).total_seconds()

        total_seconds = int(remaining)
        if total_seconds <= 0:
            print("\nTime finished!")
            break

        print(f"\rTime remaining: {total_seconds} seconds", end="")
        time.sleep(1)

    print("\nTime finished!")

countdown_timer(10)

#lab 4

import time
from datetime import datetime, timedelta

def calander(year, month):
    current_time = datetime(year, month, 1)
    start_weekday = current_time.weekday()

    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    last_month = next_month - timedelta(days=1)

    print("MON TUE WED THU FRI SAT SUN")
    print (" " * start_weekday, end="")

    while current_time <= last_month:
        print(f"{current_time.day:<3}", end="")

        if current_time.weekday() == 6:
            print()

        current_time += timedelta(days=1)

    print()


calander(2023, 1)









