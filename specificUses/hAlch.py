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
averageTimeStamped = 7.4180


def performLeftClick(mainLocation):
    global dryRun
    if (dryRun == False):
        print("Clicking at " + str(mainLocation))
        # sleepRandom(0.3, 0.7)  # remove if clicking
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

    if (random.randint(1, 1000) > 825):
        sleepRandom(0, 1)

    if (random.randint(1, 1000) > 925):
        sleepRandom(1, 2)

    if (random.randint(1, 1000) > 960):
        sleepRandom(1, 3)

    # if (random.randint(1, 1000) > 980):
    #     sleepRandom(1, 25)

    if (dryRun == False):
        time.sleep(sleep)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+4 or current[0] <= mainLoc[0]-4):
        foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            mainLoc[0] + random.randint(-3, 3),
            mainLoc[1] + random.randint(-3, 3),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6),
            random.uniform(0.6, 0.8)
        )
        current = pyautogui.position()

    return current


def castSpell(current, mainLocation):
    sleepRandom(
        random.uniform(0.3, 0.4),
        random.uniform(0.8, 1)
    )
    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation)
    sleepRandom(
        random.uniform(0.7, 1),
        random.uniform(1, 1.5)
    )
    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation)


def formatTimeLeft(timeLeft):
    # timeLeft = float(timeLeft)
    if (timeLeft > 60):
        timeLeft = round(timeLeft/60, 2)
        timeLeftMin = str(timeLeft).split('.')[0]
        timeLeftSec = (int(str(timeLeft).split('.')[1]) * 60) / 100
        if (timeLeftSec < 10):
            timeLeftSec = "0" + str(timeLeftSec)
        timeLeft = timeLeftMin + ":" + str(timeLeftSec)
    else:
        timeLeft = str(round(timeLeft, 0)) + " sec"

    return timeLeft


def clickLocations(mainLocation, item, pixelColorItem, iterations):
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
            pixelColorCurrentItem = pixelColorItem
            castSpell(pyautogui.position(), mainLocation)
        elif (dryRun == False):
            startTime = time.time()
            print("\n==== Run: " + str(i + 1) +
                  " of " + str(iterations) + " ==== " + str(iterations - (i + 1)) + " left =====")
            # timeLeft = averageTime * (iterations - i)
            # timeLeft = formatTimeLeft(timeLeft)
            # print("======== Time Left: " + timeLeft + " ========")
            foo = averageTimeStamped*(iterations - i)
            foo = formatTimeLeft(foo)
            print("======== Time Left: " +
                  str(foo) + " ========")
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
                True == True
                # str(pixelColorCurrentItem) == str(pixelColorItem)
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
            runTimeStamped = (time.time()-startTime)
            if (runTimeStamped > (averageTimeStamped*15)):
                runTimeStamped = longestRun

            if (runTimeStamped > longestRun):
                longestRun = runTimeStamped

            if (runTimeStamped < shortestRun):
                shortestRun = runTimeStamped
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Total: " + str(total))
            print("Iteration took: " + str(runTimeStamped) + "s")
            print("totalTimeStamped " + str(totalTimeStamped))
            print("longestRun " + str(longestRun))
            print("shortestRun " + str(shortestRun))
            print("averageTimeStamped " + str(averageTimeStamped))
            # guess = ((averageTime)*2)+.5
            # print("Guess: " + str(guess))
            # print("averageTime " + str(averageTime))

    return True


def run(mainLocation, item, pixelColorItem, itemCount):
    return clickLocations(mainLocation, item, pixelColorItem, itemCount)


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

    # placeHolder = input("Ready?")
    mouseOutOfRange(mainLocation)
    print("Running dry run test to assess total time")
    # success = clickLocations(
    #     mainLocation, item, pixelColorItem, dryRunItemCount)
    # averageTime = totalTime/total
    # print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Spell" + str(mainLocation))
    print("Item" + str(item))
    running = run(mainLocation, item, pixelColorItem, itemCount)
