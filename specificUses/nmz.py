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
    sleep = round(random.uniform(smallInt, largeInt), 10)*25
    sleep = sleep + round(random.uniform(3, 5), 10)
    totalTime = totalTime + sleep
    # sleep = 60 + sleep
    if (dryRun == False):
        print(sleep)

    # performLeftClick()
    if (random.randint(1, 1000) > 985):
        if (dryRun == False and random.randint(1, 10) > 4):
            pyautogui.keyDown('alt')
            pyautogui.press('tab', interval=random.uniform(0.6, 0.8) + (0.3/2))
            pyautogui.keyUp('alt')
        sleepRandom(2, 8)
        maxClick = random.randint(15, 35)
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())
    elif (random.randint(1, 1000) > 950):
        sleepRandom(1, 2)
    elif (random.randint(1, 1000) > 925):
        sleepRandom(0, 1)

    if (random.randint(1, 1000) > 920):
        maxClick = random.randint(1, 5)
        for i in range(0, maxClick):
            performLeftClick(pyautogui.position())

    if (dryRun == False):
        time.sleep(sleep)


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
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == True):
            total = total + 1
            pixelColorCurrentItem = pixelColorItem
            performClick(pyautogui.position(), mainLocation)
        elif (dryRun == False):
            print("\n============ Run: " + str(i + 1) +
                  " of " + str(iterations) + " ============")
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

            print("==== Time Left: " + timeLeft + " ====")
            mouseOutOfRange(mainLocation)
            current = pyautogui.position()
            frameinfo = getframeinfo(currentframe())
            fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
            pixelColorCurrentItem = pyautogui.screenshot(
                imageFilename=".screenshot" + fileName +
                str(frameinfo.lineno) + ".png",
                region=(
                    item[0], item[1], 1, 1
                )
            ).getcolors()

            if (
                str(pixelColorCurrentItem) == str(pixelColorItem)
            ):
                performClick(current, mainLocation)
            else:
                sleepRandom(1.3-(0.3/2), 2.7+(0.3/2))
                frameinfo = getframeinfo(currentframe())
                fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
                pixelColorCurrentItem = pyautogui.screenshot(
                    imageFilename=".screenshot" +
                    str(fileName) + str(frameinfo.lineno) + ".png",
                    region=(
                        item[0], item[1], 1, 1
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
    itemCount = input(
        "Hover over item location, how many min for run (62 recommended)? ")
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
        region=(item[0], item[1], 1, 1)
    ).getcolors()

    dryRun = True
    dryRunItemCount = 1000
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10
    success = clickLocations(
        mainLocation, item, pixelColorItem, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Main Location " + str(mainLocation))
    print("Item " + str(item))
    running = run(mainLocation, item, pixelColorItem, itemCount)
