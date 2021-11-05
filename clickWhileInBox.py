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
    # sleep = 60 + sleep
    print(sleep)

    if (random.randint(1, 1000) > 975):
        sleepRandom(0, 1)

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
    if (
        (current[0] >= mainLoc[0]+150 or
         current[0] <= mainLoc[0]-150) and
        (current[1] >= mainLoc[1]+150 or
         current[1] <= mainLoc[1]-150)
    ):
        foo = input("Move out of zone, get close and hit enter")
        sleepRandom(
            random.uniform(0.2, 0.3)-(0.3/2),
            random.uniform(0.3, 0.7) + (0.3/2)
        )


def castSpell(current, spell):
    sleepRandom(
        random.uniform(0.2, 0.3)-(0.3/2),
        random.uniform(0.3, 0.7) + (0.3/2)
    )
    mouseOutOfRange(spell)
    performLeftClick()


def clickLocations(spell, iterations):
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == True):
            total = total + 1
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
            castSpell(current, spell)
    return True


def run(spell, itemCount):
    return clickLocations(spell, itemCount)


while True == True:
    # run(spell, item, pixelColorItem, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 140

    spell = pyautogui.position()  # intention is to make two diff locations and mouse move
    item = pyautogui.position()

    dryRun = True
    dryRunItemCount = 1000
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10
    success = clickLocations(spell, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Spell" + str(spell))
    print("Item" + str(item))
    running = run(spell, itemCount)
