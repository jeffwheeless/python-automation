from datetime import datetime
import time
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re
import os

# foo = input("Hover over alternative window")
# altWindowXY = pyautogui.position()


def performLeftClick(x, y):
    sleep = round(random.uniform(0, 1), 10)
    time.sleep(sleep)
    print("Clicking")
    pyautogui.leftClick(x, y, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    sleep = round(random.uniform(smallInt, largeInt), 10)
    print(sleep)
    time.sleep(sleep)


def clickIcon(current):
    sleepRandom(60, 120)
    performLeftClick(current[0], current[1])


def clickLocations(clickableIcon, stopTime):
    now = datetime.now()
    current_time_hour = now.strftime("%H")
    current_time = now.strftime("%H:%M:%S")
    while (int(current_time_hour) <= (stopTime + 12) and int(current_time_hour) >= 8):
        print("\n=== Currently: " + current_time +
              " stopping at " + str(stopTime + 12) + ":00 ===")
        current_time_combined = int(now.strftime(
            "%H"))*60 + int(now.strftime("%M"))
        remaining_time = ((stopTime + 12) * 60) - int(current_time_combined)
        if (remaining_time > 60):
            remaining_time = round(remaining_time/60, 2)
            timeLeftHour = str(remaining_time).split('.')[0]
            timeLeftMin = (int(str(remaining_time).split('.')[1]) * 60) / 100
            if (timeLeftMin < 10):
                timeLeftMin = "0" + str(timeLeftMin)
            timeLeft = timeLeftHour + ":" + str(timeLeftMin)
        print("============= " + timeLeft + " Remainiing =============")
        current = pyautogui.position()
        clickIcon(clickableIcon)

    print("\n============ Out of office hours ============")

    return True


def run(clickableIcon, stopTime):
    return clickLocations(clickableIcon, stopTime)


while True == True:
    # run(clickableIcon, item, itemCount)
    stopTime = input("Hover over item location, what time pm to stop? ")
    clickableIcon = pyautogui.position()
    print("Icon" + str(clickableIcon))
    running = run(clickableIcon, int(stopTime))
