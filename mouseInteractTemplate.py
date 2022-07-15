import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math
from mouseAutomation import *

total = 0
totalTimeStamped = 0
averageTimeStamped = 22.760091972351074


def sleepRandom(smallInt, largeInt):
    # global totalTime
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    # print(sleep)
    time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))

    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 1)

    if (random.randint(1, 1000) > 925):
        sleepRandom(1, 2)

    if (random.randint(1, 1000) > 960):
        sleepRandom(1, 3)

    if (random.randint(1, 1000) > 995):
        sleepRandom(1, 20)


locationRuns = 5
loc = []

# loc.append([3422, 1325, '', 5, 3])
# loc.append([2753, 1230, '', 5, 1])
# loc.append([2165, 1012, '', 8, 1])
# loc.append([2218, 1557, '', 20, 8])
# loc.append([3345, 1077, '', 8, 85])

locationRuns = len(loc)

runs = 1
startAt = input("\n\nStarting location of the " + str(locationRuns) + ": ")
if (startAt == ""):
    startAt = 1
startAt = int(startAt)-1
while (True == True):

    runs = 1
    runs = int(input("How many runs: "))
    if (runs == "" or runs < 2):
        runs = 1
    else:
        runs = round(int(runs))

    print("Expected Run Time: " + str(averageTimeStamped*locationRuns*runs))
    for x in range(0, runs):
        # print("loop number:" + str(x) + " of " + str(runs))
        for temp in range(startAt, locationRuns):
            startTime = time.time()
            total = total + 1
            print("Item #" + str(temp+1) + " of " + str(locationRuns) +
                  " || " + str(loc[temp]) + " || loop number:" + str(x+1) + " of " + str(runs))

            modloc = [
                random.randint(loc[temp][0]-loc[temp][3],
                               loc[temp][0]+loc[temp][3]),
                random.randint(loc[temp][1]-loc[temp][3],
                               loc[temp][1]+loc[temp][3]),
            ]

            if (random.randint(0, 1) == 0):
                current = pyautogui.position()
                if (
                    current[0] <= modloc[0]+5 and current[0] >= modloc[0]-5 and
                    current[1] <= modloc[1]+5 and current[1] >= modloc[1]-5
                ):
                    print("Next loc is very close, staying still")
                else:
                    mouseMove(current[0], current[1], modloc[0], modloc[1])
                sleepRandom(0.05, 0.1)
                sleepRandom(loc[temp][4]-0.9, loc[temp][4]+0.5)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())
            else:
                sleepRandom(loc[temp][4]-0.9, loc[temp][4]+0.5)
                current = pyautogui.position()
                if (
                    current[0] <= modloc[0]+5 and current[0] >= modloc[0]-5 and
                    current[1] <= modloc[1]+5 and current[1] >= modloc[1]-5
                ):
                    print("Next loc is very close, staying still")
                else:
                    mouseMove(current[0], current[1], modloc[0], modloc[1])
                sleepRandom(0.1, 0.5)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())

            sleepRandom(0.1, 0.5)
            if (loc[temp][2] == '1'):
                pyautogui.press('esc')
            elif (loc[temp][2] == '2'):
                pyautogui.press('space')
            elif (loc[temp][2] == '3'):
                pyautogui.keyDown('alt')
                sleepRandom(0.1, 0.2)
                pyautogui.press('tab')
                sleepRandom(0.1, 0.2)
                pyautogui.keyUp('alt')
            sleepRandom(0.1, 0.5)

            runTimeStamped = (time.time()-startTime)
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Iteration took: " + str(runTimeStamped) + "s")

        sleepRandom(0.5, 3)
        print("Average Time Stamped took: " + str(averageTimeStamped) + "s\n")

    startAt = 0

    print("\n\n----------------------")
    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
