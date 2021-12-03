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


def performLeftClick(x, y):
    global dryRun
    if (dryRun == False):
        sleep = round(random.uniform(0, 1), 10)
        time.sleep(sleep)
        print("Clicking")
        pyautogui.leftClick(x, y, 0, random.uniform(0.3, 0.7))


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    sleep = round(random.uniform(smallInt, largeInt), 10)
    totalTime = totalTime + sleep
    print(sleep)
    if (random.randint(1, 1000) > 950):
        sleepRandom(1, 2)
    elif (random.randint(1, 1000) > 925):
        sleepRandom(0, 1)

    if (dryRun == False):
        # # if (sleep > 3):
        # #     time.sleep(sleep-3)
        # #     for i in range(3, 1):
        # #         time.sleep(1)
        # #         print(" " + str(i) + " ", end=""),
        # # else:
        time.sleep(sleep)


def castSpell(current, spell):
    sleepRandom(5, 100)
    performLeftClick(current[0], current[1])
    sleepRandom(
        random.uniform(0.7, 1)-(0.3/2),
        random.uniform(1, 1.5) + (0.3/2)
    )
    performLeftClick(current[0], current[1])


def clickLocations(spell, item, iterations):
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
            current = pyautogui.position()
            castSpell(current, spell)

    return True


def run(spell, item, itemCount):
    return clickLocations(spell, item, itemCount)


while True == True:
    # run(spell, item, itemCount)
    itemCount = input("Hover over item location, how many are there? ")
    if (type(itemCount) == str):
        itemCount = int(itemCount)
    if (itemCount <= 0):
        itemCount = 1

    spell = pyautogui.position()  # intention is to make two diff locations and mouse move
    item = pyautogui.position()

    dryRun = True
    dryRunItemCount = 500
    success = clickLocations(spell, item, dryRunItemCount)
    averageTime = totalTime/total
    print("\n\nAverage Time: " + str(averageTime))
    dryRun = False
    print("Spell" + str(spell))
    print("Item" + str(item))
    running = run(spell, item, itemCount)
