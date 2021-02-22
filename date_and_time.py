# import time
#
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location.")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d-%H:%M:%S', time.gmtime()))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())



















