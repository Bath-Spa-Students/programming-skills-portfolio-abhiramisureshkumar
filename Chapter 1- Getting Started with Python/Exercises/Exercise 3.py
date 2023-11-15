#Write a Python program to display the current date and time.

import datetime
now= datetime.date.today()
print("current date and time")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
