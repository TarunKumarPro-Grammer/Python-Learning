import time

timeHour = int(time.strftime("%H"))

if timeHour <12:
    print("Good Morining Sir")
elif timeHour > 12 and timeHour <= 18:
    print("Good Eveining Sir")
else:
    print("Good Night Sir")