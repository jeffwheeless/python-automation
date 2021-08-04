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


def performLeftClick():
    global dryRun
    if (dryRun == False):
        print("Clicking")
        pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    totalTime = totalTime + sleep
    print(sleep)

    if (random.randint(1, 1000) > 995):
        sleepRandom(10, 20)
    elif (random.randint(1, 1000) > 980):
        sleepRandom(2, 5)
    elif (random.randint(1, 1000) > 900):
        sleepRandom(1, 3)
    elif (random.randint(1, 1000) > 850):
        sleepRandom(0, 2)

    if (dryRun == False):
        if (sleep > 3):
            time.sleep(sleep-3)
            for i in range(3, 1):
                time.sleep(1)
                print(" " + str(i) + " ", end=""),
        else:
            time.sleep(sleep)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+7 or current[0] <= mainLoc[0]-7):
        foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            spell[0] + random.randint(-5, 5),
            spell[1] + random.randint(-5, 5),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6)-(0.3/2),
            random.uniform(0.6, 0.8) + (0.3/2)
        )


def castSpell(current, spell):
    sleepRandom(
        random.uniform(0.3, 0.4)-(0.3/2),
        random.uniform(0.8, 1) + (0.3/2)
    )
    mouseOutOfRange(spell)
    performLeftClick()
    sleepRandom(
        random.uniform(0.7, 1)-(0.3/2),
        random.uniform(1, 1.5) + (0.3/2)
    )
    mouseOutOfRange(spell)
    performLeftClick()


def clickLocations(spell, item, pixelColorItem, iterations):
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == True):
            total = total + 1
            pixelColorCurrentItem = pixelColorItem
            castSpell(pyautogui.position(), spell)
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
            mouseOutOfRange(spell)
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
                castSpell(current, spell)
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


def run(spell, item, pixelColorItem, itemCount):
    return clickLocations(spell, item, pixelColorItem, itemCount)


while True == True:
    # run(spell, item, pixelColorItem, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    spell = pyautogui.position()  # intention is to make two diff locations and mouse move
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
    success = clickLocations(spell, item, pixelColorItem, itemCount*10)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Spell" + str(spell))
    print("Item" + str(item))
    running = run(spell, item, pixelColorItem, itemCount)
