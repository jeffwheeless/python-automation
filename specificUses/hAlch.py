import datetime
import time
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re

# foo = input("Hover over alternative window")
# altWindowXY = pyautogui.position()
totalTime = 0.0
averageTime = 0.0
total = 0
dryRun = True


def performLeftClick():
    global dryRun
    print("Clicking")
    if (dryRun == False):
        pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    totalTime = totalTime + sleep
    print(sleep, end=" -> ")
    if (random.randint(1, 100) > 80):
        # if (dryRun == False):
        # pyautogui.press(['alt', 'tab'])
        # pyautogui.moveTo(
        # altWindowXY[0], altWindowXY[1], random.uniform(0.1, 0.2))
        sleepRandom(5, 20)
        if (random.randint(1, 100) > 75):
            sleepRandom(5, 20)
    if (dryRun == False):
        if (sleep > 3):
            time.sleep(sleep-3)
            for i in range(3, 1):
                time.sleep(1)
                print(" " + str(i) + " ", end=""),
        else:
            time.sleep(sleep)


def castSpell(current, spell):
    sleepRandom(0.3-(0.5/2), 0.9+(0.5/2))
    if (current[0] >= spell[0]+5 or current[0] <= spell[0]-5):
        pyautogui.moveTo(spell[0], spell[1], random.uniform(0.3, 0.7))
        sleepRandom(0.7-(0.3/2), 0.8+(0.3/2))
    performLeftClick()
    sleepRandom(1.5-(0.3/2), 2.0+(0.3/2))
    if (current[0] >= spell[0]+5 or current[0] <= spell[0]-5):
        pyautogui.moveTo(spell[0], spell[1], random.uniform(0.3, 0.7))
        sleepRandom(0.7-(0.3/2), 0.8+(0.3/2))
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
            print("\n============ Run: " + str(i) +
                  " of " + str(iterations) + " ============")
            current = pyautogui.position()
            timeLeft = averageTime * (iterations - i)
            if (timeLeft > 60):
                timeLeft = round(timeLeft/60, 2)
                timeLeftMin = str(timeLeft).split('.')[0]
                timeLeftSec = (int(str(timeLeft).split('.')[1]) * 60) / 100
                timeLeft = timeLeftMin + ":" + str(timeLeftSec)
            else:
                timeLeft = str(round(timeLeft, 0)) + " sec"

            print("==== Time Left: " + timeLeft + " ====")
            if (current[0] >= spell[0]+5 or current[0] <= spell[0]-5):
                pyautogui.moveTo(spell[0], spell[1], random.uniform(0.3, 0.7))
                sleepRandom(0.7-(0.3/2), 0.7+(0.3/2))
                current = pyautogui.position()

            dt = datetime.datetime.now()
            dt = datetime.datetime(
                dt.year, dt.month, dt.day, dt.hour, dt.minute)
            frameinfo = getframeinfo(currentframe())
            fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
            pixelColorCurrentItem = pyautogui.screenshot(
                imageFilename=".screenshot" + fileName + str(dt) + ".png",
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
                dt = datetime.datetime.now()
                dt = datetime.datetime(
                    dt.year, dt.month, dt.day, dt.hour, dt.minute)
                pixelColorCurrentItem = pyautogui.screenshot(
                    imageFilename=".screenshot" +
                    str(fileName) + str(dt) + ".png",
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


# foo = input("Hover over spell location")
# spell = pyautogui.position()
# itemCount = input("Hover over item location, how many are there? ")
# if (type(itemCount) != int):
#     itemCount = int(itemCount)

# item = pyautogui.position()
# dt = datetime.datetime.now()
# dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
# pixelColorItem = pyautogui.screenshot(
#     imageFilename=".screenshot" + str(dt) + ".png",
#     region=(item[0], item[1], 1, 1)


# ).getcolors()

# dryRun = True
# success = clickLocations(spell, item, pixelColorItem, itemCount*10)
# averageTime = totalTime/total
# print("\n\nAverage Time: " + str(averageTime))
# dryRun = False
# print("Spell" + str(spell))
# print("Item" + str(item))
foo = input("Hover over spell location")
spell = pyautogui.position()
while True == True:
    # run(spell, item, pixelColorItem, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    item = pyautogui.position()
    frameinfo = getframeinfo(currentframe())
    fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
    dt = datetime.datetime.now()
    dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
    pixelColorItem = pyautogui.screenshot(
        imageFilename=".screenshot" + str(fileName) + str(dt) + ".png",
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
