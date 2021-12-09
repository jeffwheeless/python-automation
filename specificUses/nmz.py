import datetime
import time
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re
import os

# foo = input("Hover over alternative window")
# altWindowXY = pyautogui.position()
totalTime = 0.0
averageTime = 0.0
total = 0
dryRun = True


def performLeftClick(mainLocation):
    global dryRun
    if (dryRun == False):
        sleep = round(random.uniform(0, 1), 10)
        time.sleep(sleep)
        print("Clicking")
        pyautogui.leftClick(
            mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    sleep = sleep + round(random.uniform(3, 5), 10)
    totalTime = totalTime + sleep
    # sleep = 60 + sleep
    # print(sleep)
    if (sleep >= 60):
        maxClick = random.randint(1, int((sleep/2)/10))
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())
    elif (random.randint(1, 1000) > 960):
        maxClick = random.randint(1, 2)
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())

    if (dryRun == False):
        print(sleep)
        time.sleep(sleep)

    if (sleep >= 60):
        maxClick = random.randint(1, int((sleep/2)/10))
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())
    elif (random.randint(1, 1000) > 960):
        maxClick = random.randint(1, 2)
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+7 or current[0] <= mainLoc[0]-7):
        # foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            mainLoc[0] + random.randint(-5, 5),
            mainLoc[1] + random.randint(-5, 5),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6)-(0.3/2),
            random.uniform(0.6, 0.8) + (0.3/2)
        )
        current = pyautogui.position()

    return current


def performClick(current, mainLocation):
    totalTimeClicking = 0
    while (totalTimeClicking <= 55):
        smallTime = 1
        largeTime = 2
        timeSlot = random.randint(1, 4)
        if (timeSlot == 4 and totalTimeClicking+30 < 55):
            smallTime = random.uniform(15, 20)
            largeTime = random.uniform(21, 30)
            if (random.randint(1, 10) > 7):
                mainLocation = mouseOutOfRange(mainLocation)
                performLeftClick(mainLocation)
                smallTime = random.uniform(45, 60)
                largeTime = random.uniform(75, 90)
            elif (random.randint(1, 10) > 7):
                mainLocation = mouseOutOfRange(mainLocation)
                performLeftClick(mainLocation)
                smallTime = random.uniform(60, 90)
                largeTime = random.uniform(110, 140)
        elif (timeSlot == 3 and totalTimeClicking+15 < 55):
            smallTime = random.uniform(7, 12)
            largeTime = random.uniform(13, 15)
        elif (timeSlot == 2 and totalTimeClicking+10 < 55):
            smallTime = random.uniform(5, 7)
            largeTime = random.uniform(8, 10)
        elif (timeSlot == 0):
            smallTime = random.uniform(0, 0.9)
            largeTime = random.uniform(1, 2)
        elif (totalTimeClicking < 55):
            smallTime = (55-totalTimeClicking)/2
            largeTime = 55-totalTimeClicking
        else:
            return True

        totalTimeClicking = totalTimeClicking + largeTime
        sleepRandom(
            smallTime,
            largeTime
        )
        mainLocation = mouseOutOfRange(mainLocation)
        performLeftClick(mainLocation)


def clickLocations(mainLocation, item, iterations):
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == True):
            total = total + 1
            performClick(pyautogui.position(), mainLocation)
        elif (dryRun == False):
            print("\n============ Run: " + str(i + 1) +
                  " of " + str(iterations) + " ============")
            timeLeft = averageTime * (iterations - i)
            timeLeftMin = round((timeLeft) // 60)
            timeLeftSec = ("0" if ((timeLeft) % 60) <
                           10 else "") + str(round(timeLeft % 60, 5))
            timeLeftStr = str(timeLeftMin) + ":" + str(timeLeftSec)
            print("==== Time Left: " + timeLeftStr + " ====")
            mainLocation = mouseOutOfRange(mainLocation)
            current = pyautogui.position()
            performClick(current, mainLocation)

    return True


def run(mainLocation, item, itemCount):
    return clickLocations(mainLocation, item, itemCount)


while True == True:
    # run(mainLocation, item, itemCount)
    itemCount = input(
        "Hover over item location, how many min for run (80 prob. max)? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    # intention is to make two diff locations and mouse move
    mainLocation = pyautogui.position()
    item = pyautogui.position()
    dryRun = True
    dryRunItemCount = 500
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10
    success = clickLocations(
        mainLocation, item, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Main Location " + str(mainLocation))
    print("Item " + str(item))
    running = run(mainLocation, item, itemCount)
    print("\nTotal Time: " +
          str(int((itemCount*averageTime) // 60)) + ":" +
          ("0" if ((itemCount*averageTime) % 60) < 10 else "") +
          str(round((itemCount*averageTime) % 60, 5))
          )
