from datetime import datetime
import time
import pyautogui
import random
import math
from inspect import currentframe, getframeinfo
import re
import os

# foo = input("Hover over alternative window")
# altWindowXY = pyautogui.position()

latestDaysHour = 8


def performLeftClick(x, y):
    sleep = round(random.uniform(1, 2), 0)
    time.sleep(sleep)
    print("Clicking")
    pyautogui.leftClick(x, y, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    sleep = round(random.randint(smallInt, largeInt), 0)
    print("Sleeping for: " + str(sleep // 60) + ":" + str(sleep % 60))
    time.sleep(sleep)


def clickIcon(current):
    sleepRandom(60, 120)
    performLeftClick(current[0], current[1])
    performLeftClick(current[0], current[1])


def clickLocations(clickableIcon, stopTime):
    global latestDaysHour
    now = datetime.now()
    current_time_hour = int(now.strftime("%H"))
    print("\n=== Currently: \t" + now.strftime("%H:%M") + "\t =====")
    if ((current_time_hour > stopTime and current_time_hour >= latestDaysHour)):
        print("Stop time entered has passed and isn't within working hours")
        return False

    while (current_time_hour > stopTime and current_time_hour < latestDaysHour):
        print("XXXX Out of office hours XXXXX")
        sleepRandom(1800, 3600)
        current_time_hour = int(now.strftime("%H"))
        print("\n=== Currently: \t" + now.strftime("%H:%M") + "\t =====")

    while (current_time_hour <= stopTime and current_time_hour >= latestDaysHour):
        print("=== Stop At: \t" + (str(stopTime) if (stopTime <= 12)
              else str(stopTime - 12)) + ":00\t =====")
        remaining_time = (stopTime * 60) - \
            (current_time_hour*60 + int(now.strftime("%M")))
        remaining_time_display = str(
            remaining_time // 60) + ":" + str(remaining_time % 60)
        print("=== Remaining: \t" + remaining_time_display + "\t =====")
        clickIcon(clickableIcon)
        current_time_hour = int(now.strftime("%H"))
        print("\n=== Currently: \t" + now.strftime("%H:%M") + "\t =====")

    return True


def run(clickableIcon, stopTime):
    global latestDaysHour
    if (int(stopTime) < latestDaysHour):  # should be 12 but changed to 8 to rep hours that are workable
        stopTime = int(stopTime) + 12
    return clickLocations(clickableIcon, stopTime)


while True == True:
    # run(clickableIcon, item, itemCount)
    stopTime = input("Hover over item location, what time pm to stop: \t")
    clickableIcon = pyautogui.position()
    print("Icon" + str(clickableIcon))
    running = True
    while (running == True):
        running = run(clickableIcon, int(stopTime))
