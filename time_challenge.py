import pytz

timezones = {1: {"zone": "Great Britain", "timezone": 'GB'},
             2: {"zone": "Greece", "timezone": 'Europe/Athens'},
             3: {"zone": "Spain", "timezone": 'Europe/Madrid'},
             4: {"zone": "France", "timezone": 'Europe/Paris'},
             5: {"zone": "Italy", "timezone": 'Europe/Rome'},
             6: {"zone": "Croatia", "timezone": 'Europe/Zagreb'},
             7: {"zone": "Sweden", "timezone": 'Europe/Stockholm'},
             8: {"zone": "Finland", "timezone": 'Europe/Helsinki'},
             9: {"zone": "Belgium", "timezone": 'Europe/Brussels'},
             }

for location in sorted(timezones):
    print("{}: {}".format(location, timezones[location]["zone"]))

print()
user = None

while user != 0:
    try:
        print("You can anytime press 0 to quit.")
        user = int(input("Please enter a timezone from 1-9: "))

        if user in timezones.keys():
            tzToDisplay = pytz.timezone(timezones[user]["timezone"])
            print("Here you go: ")
            print()
            print(f"Your local time is: {pytz.datetime.datetime.now().strftime('%A %x %X')}")
            print(f"Your UTC local time is: {pytz.datetime.datetime.utcnow().strftime('%A %x %X')}")
            print("Your chosen zone: {}\t The time: {}".format(timezones[user]["zone"],
                                                               pytz.datetime.datetime.now(tzToDisplay).strftime(
                                                                   '%A %x %X')))
            print("=" * 50)
            continue

        elif user == 0:
            print("Alright, you chose to quit")
            break

        else:
            print("Sorry, that is invalid.")
            print()
            continue

    except (ValueError, TypeError):
        print("Sorry, but you have to enter an integer from 1-9, or 0, not anything else!")
        print()
        continue
