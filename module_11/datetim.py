import datetime

current_datetime = datetime.datetime.now()

print(current_datetime)

print("Year: ", current_datetime.year)
print("Month: ", current_datetime.month)
print("Day: ", current_datetime.day)
print("Hour: ", current_datetime.hour)
print("Minute: ", current_datetime.minute)
print("Microsecond: ", current_datetime.microsecond)

current_date = datetime.datetime.now().date()

print(current_date)
print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)

# Get the current time
current_time = datetime.datetime.now().time()

print(current_time)
print("Hour: ", current_time.hour)
print("Minute: ", current_time.minute)
print("Second: ", current_time.second)
print("Microsecond: ", current_time.microsecond)

# Get a specific date
specific_date = datetime.date(year=2024, month=4, day=5)

# Get a specific time
specific_time = datetime.time(hour=12, minute=30, second=0)

print(specific_date)
print(specific_time)

duration = datetime.timedelta(days=5,hours=3)

new_date = current_datetime + duration
print(new_date)

previous_date= current_datetime - duration
print(previous_date)

import datetime


utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC time: ", utc_time)

custom_offset = datetime.timedelta(hours=3)

custom_time = utc_time.replace(tzinfo=datetime.timezone(custom_offset))
print("Current time in custom time zone (UTC + 3): ", custom_time)
































