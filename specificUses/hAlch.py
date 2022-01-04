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
        print("Clicking at " + str(mainLocation))
        pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    # sleep = sleep + round(random.uniform(0.5, 1.2), 10) # enable if on virtual machine
    totalTime = totalTime + sleep
    # sleep = 60 + sleep
    if (dryRun == False):
        print(sleep)

    if (random.randint(1, 1000) > 965):
        sleepRandom(0, 1)
    elif (random.randint(1, 1000) > 975):
        sleepRandom(1, 2)

    if (dryRun == False):
        time.sleep(sleep)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+4 or current[0] <= mainLoc[0]-4):
        # foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            mainLoc[0] + random.randint(-3, 3),
            mainLoc[1] + random.randint(-3, 3),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6)-(0.3/2),
            random.uniform(0.6, 0.8) + (0.3/2)
        )
        current = pyautogui.position()

    return current


def castSpell(current, mainLocation):
    sleepRandom(
        random.uniform(0.3, 0.4)-(0.3/2),
        random.uniform(0.8, 1) + (0.3/2)
    )
    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation)
    sleepRandom(
        random.uniform(0.7, 1)-(0.3/2),
        random.uniform(1, 1.5) + (0.3/2)
    )
    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation)


def clickLocations(mainLocation, item, pixelColorItem, iterations):
    global total, averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == True):
            total = total + 1
            pixelColorCurrentItem = pixelColorItem
            castSpell(pyautogui.position(), mainLocation)
        elif (dryRun == False):
            print("\n==== Run: " + str(i + 1) +
                  " of " + str(iterations) + " ==== " + str(iterations - (i + 1)) + " left =====")
            timeLeft = averageTime * (iterations - i)
            if (timeLeft > 60):
                timeLeft = round(timeLeft/60, 2)
                timeLeftMin = str(timeLeft).split('.')[0]
                timeLeftSec = (int(str(timeLeft).split('.')[1]) * 60) / 100
                if (timeLeftSec < 10):
                    timeLeftSec = "0" + str(timeLeftSec)
                timeLeft = timeLeftMin + ":" + str(timeLeftSec)
            else:
                timeLeft = str(round(timeLeft, 0)) + " sec"

            print("======== Time Left: " + timeLeft + " ========")
            mouseOutOfRange(mainLocation)
            current = pyautogui.position()
            frameinfo = getframeinfo(currentframe())
            fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
            pixelColorCurrentItem = pyautogui.screenshot(
                imageFilename=".screenshot" + fileName +
                str(frameinfo.lineno) + ".png",
                region=(
                    item[0], item[1], 10, 10
                )
            ).getcolors()

            if (
                str(pixelColorCurrentItem) == str(pixelColorItem)
            ):
                castSpell(current, mainLocation)
            else:
                sleepRandom(1.3-(0.3/2), 2.7+(0.3/2))
                frameinfo = getframeinfo(currentframe())
                fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
                pixelColorCurrentItem = pyautogui.screenshot(
                    imageFilename=".screenshot" +
                    str(fileName) + str(frameinfo.lineno) + ".png",
                    region=(
                        item[0], item[1], 10, 10
                    )
                ).getcolors()
                if (
                    str(pixelColorCurrentItem) != str(pixelColorItem)
                ):
                    print("wrong color return false")
                    print(str(pixelColorCurrentItem) +
                          " != " + str(pixelColorItem))

                    restart = input("continue (y|n)")
                    if (restart == 'y' or restart == 'Y'):
                        continue
                    else:
                        return False

    return True


def run(mainLocation, item, pixelColorItem, itemCount):
    return clickLocations(mainLocation, item, pixelColorItem, itemCount)


while True == True:
    # run(mainLocation, item, pixelColorItem, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    # intention is to make two diff locations and mouse move
    mainLocation = pyautogui.position()
    item = pyautogui.position()
    frameinfo = getframeinfo(currentframe())
    fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
    dt = datetime.datetime.now()
    dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
    pixelColorItem = pyautogui.screenshot(
        imageFilename=".screenshot" +
        str(fileName) + str(frameinfo.lineno) + ".png",
        region=(item[0], item[1], 10, 10)
    ).getcolors()

    dryRun = True
    dryRunItemCount = 1000
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10

    placeHolder = input("Ready?")
    mouseOutOfRange(mainLocation)
    print("Running dry run test to assess total time")
    success = clickLocations(
        mainLocation, item, pixelColorItem, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Spell" + str(mainLocation))
    print("Item" + str(item))
    running = run(mainLocation, item, pixelColorItem, itemCount)
