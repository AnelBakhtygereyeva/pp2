#1 - Write a Python program to subtract five days from current date.
"""
from datetime import datetime, timedelta

current = datetime.now().date()

new = current - timedelta(days=5)

print("current:", current) #prints current date and time
print("new:", new) #prints date when substracting 5 days from current
"""

#2 - Write a Python program to print yesterday, today, tomorrow.
"""
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(" yesterday:",yesterday, "\n", "today:", today, "\n", "tomorrow:", tomorrow)
"""

#3 - Write a Python program to drop microseconds from datetime.
"""
from datetime import datetime

date = datetime.now()

drop_microseconds = date.replace(microsecond=0)

print(" date: ", date, "\n", "date without microseconds: ", drop_microseconds)
"""

#4 - Write a Python program to calculate two date difference in seconds.
"""
from datetime import datetime

dateInput1 = input("(YYYY-MM-DD HH:MM:SS): ")
dateInput2 = input("(YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(dateInput1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(dateInput2, "%Y-%m-%d %H:%M:%S")

differenceInSeconds = (date2 - date1).total_seconds()

print("difference in seconds: ", differenceInSeconds)
"""