import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math
from mouseAutomation import *
from inventory import *

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

    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 0.5)

    if (sleep > 0.5):
        if (random.randint(1, 1000) > round(925-largeInt)):
            sleepRandom(1, 2)

        if (random.randint(1, 1000) > round(960-largeInt)):
            sleepRandom(1, 3)

        # if (random.randint(1, 1000) > round(990-largeInt)):
        #     sleepRandom(1, 20)


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
loc.append([1511, 720, '', 5, 1])
loc.append([1972, 945, '', 5, 1])
loc.append([3476, 864, '', 5, 1])
loc.append([4640, 623, '', 5, 1])
loc.append([5493, 1075, '', 5, 1])
loc.append([1940, 1329, '', 5, 1])

locationRuns = len(loc)

verbose = 'n'  # input("\nRun program verbosly? (y/n) ")
print("\nPercision for sleep timer:")
variance = int(
    input("0) none  1) 0.5/1.5  2) 0.8/1.2  3) 0.95/1.05\nChoice: "))
# input("\n\nStarting location of the " + str(locationRuns) + ": ")
startAt = 1
if (startAt == ""):
    startAt = 1
startAt = int(startAt)-1
while (True == True):
    runs = input("How many runs: ")
    if (runs == "" or int(runs) < 2):
        runs = 1
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
                if (random.randint(0, 10) >= 1 and locationRuns > 2):
                    randomLocation = random.randint(0, locationRuns-1)
                    randomModloc = [
                        random.randint(loc[randomLocation][0]-30,
                                       loc[randomLocation][0]+30),
                        random.randint(loc[randomLocation][1]-30,
                                       loc[randomLocation][1]+30),
                    ]
                    current = pyautogui.position()
                    mouseMove(current[0], current[1],
                              randomModloc[0], randomModloc[1])

                current = pyautogui.position()
                mouseMove(current[0], current[1], modloc[0], modloc[1])
                if (waitTime == 0):
                    sleepRandom(0.05, 0.1)
                elif (random.randint(0, 1) == 0):
                    sleepRandom(waitTime-0.9, waitTime+0.5)
                else:
                    variantSleep(variance, waitTime)

                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())

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
                    clickInventory([])
                    pass

                if (verbose.lower() == "y" or verbose.lower() == "yes"):
                    print("Pressing key: " + str(loc[temp][2]))

                pyautogui.press(loc[temp][2])

            if (waitTime == 0):
                sleepRandom(0.05, 0.1)
            else:
                sleepRandom(0.1, 0.5)

            runTimeStamped = (time.time()-startTime)
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Iteration took: " + str(runTimeStamped) + "s")

        # sleepRandom(0.5, 3)
        print("\nAverage Time Stamped took: " +
              str(averageTimeStamped) + "s\n")

    startAt = 0

    print("\n\n----------------------")
