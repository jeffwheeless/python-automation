import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

from modules.mouseAutomation import MouseAutomation
from modules.inventory import Inventory

verbose = 'F'
total = 0
totalTimeStamped = 0
averageTimeStamped = 22.760091972351074


def sleepRandom(smallInt, largeInt):
    global verbose
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    if (verbose.lower() == "y" or verbose.lower() == "yes"):
        print(sleep)

    time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))

    if (random.randint(1, 1000) > 500):
        sleepRandom(0, 0.01)
        
    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 0.5)

    # if (sleep > 0.5):
    #     if (random.randint(1, 1000) > round(925-largeInt)):
    #         sleepRandom(1, 2)

    #     if (random.randint(1, 1000) > round(960-largeInt)):
    #         sleepRandom(1, 3)

    #     # if (random.randint(1, 1000) > round(990-largeInt)):
    #     #     sleepRandom(1, 20)


def variantSleep(variance, timer):
    if (timer == 0):
        sleepRandom(0.05, 0.1)
    elif (variance == 0):
        sleepRandom(timer*.98, timer*1.01)
    elif (variance == 1):
        sleepRandom(timer*.5, timer*1.5)
    elif (variance == 2):
        sleepRandom(timer*.8, timer*1.2)
    elif (variance == 3):
        sleepRandom(timer*.95, timer*1.05)
    else:
        sleepRandom(0, timer*2)


loc = []
loc.append([1193, 648, '', 6, 0])

loc2 = []
loc2.append([1433, 514, '', 5, 1])

locationRuns = len(loc)

verbose = input("\nRun program verbosly? (y/n) ")
print("\nPercision for sleep timer:")
variance = int(
    input("0) none  1) 0.5/1.5  2) 0.8/1.2  3) 0.95/1.05\nChoice: "))
# input("\n\nStarting location of the " + str(locationRuns) + ": ")
startAt = 1
if (startAt == ""):
    startAt = 1
startAt = int(startAt)-1
increasingChange = 0
while (True == True):

    runs = 1
    runs = input("How many runs: ")
    if (runs == "" or int(runs) < 2):
        # runs = 1
        runs = random.randint(150, 500)
        runs = random.randint(500, 1000)
    else:
        runs = round(int(runs))

    print("Expected Run Time: " + str(averageTimeStamped*locationRuns*runs))
    for x in range(0, runs):
        # print("loop number:" + str(x) + " of " + str(runs))
        for temp in range(startAt, locationRuns):
            waitTime = loc[temp][4]
            if (x == 0 and temp == 0):
                waitTime = 1
            startTime = time.time()
            total = total + 1
            timeLeft = round(averageTimeStamped *
                             ((locationRuns*runs)-((x+1)*(temp+1))))
            totalTimeLeft = ("Total Time: " +
                             str(int((timeLeft) // 60)) + ":" +
                             ("0" if ((timeLeft) % 60) < 10 else "") +
                             str(round((timeLeft) % 60, 5)))
            print("\n" + str(loc[temp]) + " || " + "Item #" + str(temp+1) + " of " + str(
                locationRuns) + " || loop:" + str(x+1) + " of " + str(runs) + " || " + totalTimeLeft)

            modloc = [
                random.randint(loc[temp][0]-loc[temp][3],
                               loc[temp][0]+loc[temp][3]),
                random.randint(loc[temp][1]-loc[temp][3],
                               loc[temp][1]+loc[temp][3]),
            ]

            if (loc[temp][1] != 0 and loc[temp][1] != 0):
                if (random.randint(0, 1) == 0):
                    current = pyautogui.position()
                    MouseAutomation.mouseMove(current[0], current[1], modloc[0], modloc[1])
                    variantSleep(variance, waitTime)
                    MouseAutomation.mouseOutOfRange(modloc)
                    MouseAutomation.performLeftClick(pyautogui.position())
                else:
                    if (waitTime == 0):
                        # sleepRandom(0.05, 0.1)
                        sleepRandom(0.01, 0.05)
                    else:
                        sleepRandom(waitTime-0.9, waitTime+0.5)

                    current = pyautogui.position()
                    MouseAutomation.mouseMove(current[0], current[1], modloc[0], modloc[1])
                    sleepRandom(0.1, 0.5)
                    MouseAutomation.mouseOutOfRange(modloc)
                    MouseAutomation.performLeftClick(pyautogui.position())

            if (loc[temp][2] != ''):
                sleepRandom(0.5, 0.9)
                if (loc[temp][2] == "alttab"):
                    pyautogui.keyDown('alt')
                    sleepRandom(0.1, 0.2)
                    pyautogui.press('tab')
                    sleepRandom(0.1, 0.2)
                    pyautogui.keyUp('alt')
                    pass
                elif (loc[temp][2] == 'clickinv'):
                    Inventory.clickInventory([0, 26])
                    pass

                if (verbose.lower() == "y" or verbose.lower() == "yes"):
                    print("Pressing key: " + str(loc[temp][2]))

                pyautogui.press(loc[temp][2])

            if (waitTime == 0):
                # sleepRandom(0.05, 0.1)
                sleepRandom(0.01, 0.05)
            else:
                sleepRandom(0.1, 0.5)

            runTimeStamped = (time.time()-startTime)
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Iteration took: " + str(runTimeStamped) + "s")
            
            # if (random.randint(1, 1000) > 980):
            increasingChange = increasingChange + 1
            if (random.randint(1, 1000) > (1000 - increasingChange)):
                current = pyautogui.position()
                modloc2 = [
                    random.randint(loc2[0][0]-loc2[0][3],
                                    loc2[0][0]+loc2[0][3]),
                    random.randint(loc2[0][1]-loc2[0][3],
                                    loc2[0][1]+loc2[0][3]),
                ]
                MouseAutomation.mouseMove(current[0], current[1], modloc2[0], modloc2[1])
                sleepRandom(0.1, 0.5)
                MouseAutomation.mouseOutOfRange(modloc2)
                MouseAutomation.performLeftClick(pyautogui.position())
                increasingChange = 0

        # sleepRandom(0.5, 3)
        print("\nAverage Time Stamped took: " +
              str(averageTimeStamped) + "s\n")

    startAt = 0

    current = pyautogui.position()
    modloc2 = [
        random.randint(loc2[0][0]-loc2[0][3],
                        loc2[0][0]+loc2[0][3]),
        random.randint(loc2[0][1]-loc2[0][3],
                        loc2[0][1]+loc2[0][3]),
    ]
    MouseAutomation.mouseMove(current[0], current[1], modloc2[0], modloc2[1])
    sleepRandom(0.1, 0.5)
    MouseAutomation.mouseOutOfRange(modloc2)
    MouseAutomation.performLeftClick(pyautogui.position())
    print("\n\n----------------------")
    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
