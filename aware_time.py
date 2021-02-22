import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time: {local_time}")
print(f"Naive UTC time: {utc_time}")

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time: {aware_local_time}\t timezone: {aware_local_time.tzinfo}")
print(f"Aware UTC time: {aware_utc_time}\t timezone: {aware_utc_time.tzinfo}")

gap_time = datetime.datetime(2020, 11, 19, 7, 18, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1605770280.0
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(f"{s} seconds since the epoch is {dt1}")
print(f"{t} seconds since the epoch is {dt2}")






















