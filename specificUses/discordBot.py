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


def performLeftClick(mainLocation, repeatedWord=""):
    global dryRun
    mainLocation = mouseOutOfRange(mainLocation)
    if (dryRun == False):
        sleep = round(random.uniform(0, 1), 10)
        time.sleep(sleep)
        print("Clicking")
        pyautogui.leftClick(
            mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
        if (repeatedWord != ""):
            pyautogui.write(str(repeatedWord))
            pyautogui.press('enter')


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


def performClick(current, mainLocation, repeatedWord=""):
    totalTimeClicking = 0
    while (totalTimeClicking <= 55):
        smallTime = 1
        largeTime = 2
        smallTime = random.uniform(32*1*1, 45*1*1)
        largeTime = random.uniform(60*1*1, 72*1*1)
        if (random.randint(1, 10) > 8):
            mainLocation = mouseOutOfRange(mainLocation)
            performLeftClick(mainLocation)
            smallTime = random.uniform(45*1*1, 55*1*1)
            largeTime = random.uniform(65*1*1, 80*1*1)
        elif (random.randint(1, 10) > 9):
            mainLocation = mouseOutOfRange(mainLocation)
            performLeftClick(mainLocation)
            smallTime = random.uniform(55*1*1, 65*1*1)
            largeTime = random.uniform(72*1*1, 90*1*1)

        totalTimeClicking = totalTimeClicking + largeTime
        sleepRandom(
            smallTime,
            largeTime
        )
        mainLocation = mouseOutOfRange(mainLocation)
        performLeftClick(mainLocation, repeatedWord)


def clickLocations(mainLocation, repeatedWord, iterations):
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
            performClick(current, mainLocation, repeatedWord)
    return True


def run(mainLocation, repeatedWord, itemCount):
    return clickLocations(mainLocation, repeatedWord, itemCount)


while True == True:
    # run(mainLocation, item, itemCount)
    itemCount = input(
        "Hover over item location, how many min for run (~2 run/hr)? ")
    repeatedWord = input("Repeat what command? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    # intention is to make two diff locations and mouse move
    mainLocation = pyautogui.position()
    dryRun = True
    dryRunItemCount = 5
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10
    success = clickLocations(
        mainLocation, repeatedWord, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Main Location " + str(mainLocation))
    print("Item " + str(repeatedWord))
    running = run(mainLocation, repeatedWord, itemCount)
    print("\nTotal Time: " +
          str(int((itemCount*averageTime) // 60)) + ":" +
          ("0" if ((itemCount*averageTime) % 60) < 10 else "") +
          str(round((itemCount*averageTime) % 60, 5))
          )
