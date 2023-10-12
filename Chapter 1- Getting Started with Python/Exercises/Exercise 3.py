#Write a Python program to display the current date and time.

import datetime
current_date = datetime.date.today()
print("current date ; ", current_date)

currrent_time = datetime.datetime.now().time()
print("current time  :" , current_time )