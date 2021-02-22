# import time
#
# print(time.gmtime(0))
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

import time
from time import perf_counter as my_timer
import random

input("Press enter to start: ")

wait_time = random.randint(1, 10)
print("PLease wait for " + str(wait_time) + " seconds")
time.sleep(wait_time)
start_time = my_timer()
input("Please press enter to stop: ")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds")















