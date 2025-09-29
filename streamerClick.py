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
runTimeStamped = 0
totalTimeStamped = 0
longestRun = 0
shortestRun = 100
averageTimeStamped = 4.942100568860769


def performLeftClick(mainLocation):
    global dryRun
    if (dryRun == False):
        print("\nClicking at " + str(mainLocation))
        sleepRandom(0, 0.0001)  # remove if clicking
        pyautogui.leftClick(None, None, 0, random.uniform(0, 0.0002))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    print("Sleep  " + str(sleep))
    # sleep = sleep + round(random.uniform(0.5, 1.2), 10) # enable if on virtual machine
    # sleep = 60 + sleep
    # sleepRandom(30, 60)
    if (random.randint(1, 100) > 50):
        sleepRandom(0, 0.005)

    if (random.randint(1, 100) > 80):
        sleepRandom(0, 0.05)

    if (random.randint(1, 100) > 90):
        sleepRandom(0, 0.1)

    if (random.randint(1, 1000) > 980):
        sleepRandom(0, 1)

    #     if (random.randint(1, 10000) > 9990):
    #         sleepRandom(1, 100)

    if (dryRun == False):
        time.sleep(sleep)


def castSpell(current, mainLoc):
    performLeftClick(mainLoc)


def clickLocations(mainLoc, item, iterations):
    global total, averageTime
    global dryRun
    global runTimeStamped
    global totalTimeStamped
    global averageTimeStamped
    global longestRun
    global shortestRun
    for i in range(0, iterations): 
        total = total + 1
        if (False == True and dryRun == True):
            total = total + 1
            # pixelColorCurrentItem = pixelColorItem
            castSpell(pyautogui.position(), mainLoc)
        elif (dryRun == False):
            current = pyautogui.position()
            if (current[0] >= mainLoc[0]+25 or current[0] <= mainLoc[0]-25):
                foo = input("Move out of zone, get close and hit enter")
            current = pyautogui.position()
            castSpell(current, mainLoc)

    return True


def run(mainLocation, item, itemCount):
    return clickLocations(mainLocation, item, itemCount)


while True == True:
    # run(mainLocation, item, pixelColorItem, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (itemCount == "" or itemCount == "0"):
        itemCount = random.randint(250, 999)
    if (type(itemCount) == str):
        itemCount = int(itemCount)

    # intention is to make two diff locations and mouse move
    mainLocation = pyautogui.position()
    item = pyautogui.position()
    dryRun = True
    dryRunItemCount = 1000
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10

    # placeHolder = input("Ready?")
    print("Running dry run test to assess total time")
    dryRun = False
    print("Spell" + str(mainLocation))
    print("Item" + str(item))
    running = run(mainLocation, item, itemCount)
