#Program to  get current time using date time function

import datetime
now = datetime.datetime.now()
print("Today's Date = ",end = "")
print(now.strftime("%d-%m-%Y"))