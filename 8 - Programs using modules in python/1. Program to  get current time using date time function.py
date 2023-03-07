#Program to  get current time using date time function

import datetime
now = datetime.datetime.now()
print("current Time = ",end = "")
print(now.strftime("%H:%M:%S"))