from datetime import datetime
import time
import pyautogui
import random

latestDaysHour = 20
earliestDaysHour = 7


def performLeftClick(x, y):
    sleep = round(random.uniform(1, 2), 0)
    time.sleep(sleep)
    print("Clicking")
    pyautogui.leftClick(x, y, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    sleep = round(random.randint(smallInt, largeInt), 0)
    print("Sleeping for: " + str(sleep // 60) + ":" +
          ("0" if (sleep % 60) < 10 else "") + str(sleep % 60))
    time.sleep(sleep)


def clickIcon(current):
    sleepRandom(60, 120)
    performLeftClick(current[0], current[1])
    performLeftClick(current[0], current[1])


def clickLocations(clickableIcon):
    global latestDaysHour
    global earliestDaysHour
    now = datetime.now()
    current_time_hour = int(datetime.now().strftime("%H"))
    print("\n=== Currently: \t" + datetime.now().strftime("%H:%M") + "\t =====")
    while (current_time_hour < earliestDaysHour or current_time_hour > latestDaysHour):
        print("XXXX Out of office hours XXXXX")
        sleepRandom(1800, 3600)
        current_time_hour = int(datetime.now().strftime("%H"))
        print("\n=== Currently: \t" +
              datetime.now().strftime("%H:%M") + "\t =====")

    while (current_time_hour >= earliestDaysHour and current_time_hour <= latestDaysHour):
        print("=== Stop At: \t" + str(latestDaysHour-12) + ":00\t =====")
        remaining_time = (latestDaysHour * 60) - \
            (current_time_hour*60 + int(datetime.now().strftime("%M")))
        remaining_time_display = str(
            remaining_time // 60) + ":" + ("0" if (remaining_time % 60) < 10 else "") + str(remaining_time % 60)

        print("=== Remaining: \t" + remaining_time_display + "\t =====")
        clickIcon(clickableIcon)
        current_time_hour = int(datetime.now().strftime("%H"))
        print(current_time_hour)
        print("\n=== Currently: \t" +
              datetime.now().strftime("%H:%M") + "\t =====")

    print("EOD detected, restarting to go tomorrow")
    return True


while True == True:
    stopTime = input("Hover over item location and press enter ")
    clickableIcon = pyautogui.position()
    print("Mouse Location: " + str(clickableIcon))
    running = True
    while (running == True):
        running = clickLocations(clickableIcon)
