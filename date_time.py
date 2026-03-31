from datetime import datetime

# get current date and time
now = datetime.now()

print("Current date and time:", now)

# get only date
print("Today's date:", now.date())

# get only time
print("Current time:", now.time())