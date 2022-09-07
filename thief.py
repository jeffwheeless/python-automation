import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

import sys
import os
import pathlib
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/modules')
from configHelper import *
from mouseAutomation import *
from inventory import *

total = 0
totalTimeStamped = 0

def sleepRandom(smallInt, largeInt):
    global verbose
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))
    if (verbose.lower() == "y" or verbose.lower() == "yes"):
        print(sleep)

    time.sleep(sleep)
    
    if (random.randint(1, 1000) > 400):
        sleepRandom(0, 0.01)

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
        sleepRandom(timer*.98, timer*1.02)
    elif (variance == 1):
        sleepRandom(timer*.90, timer*1.1)
    elif (variance == 2):
        sleepRandom(timer*.75, timer*1.25)
    elif (variance == 3):
        sleepRandom(timer*.5, timer*1.5)
    else:
        sleepRandom(timer-0.9, timer+0.5)



def setNumberInputToDefaultIfNone(userInput, defaultNumber = False):
    try:
        return int(userInput)
    except:
        if (defaultNumber == False):
            defaultNumber = random.randint(50, 400)
                        
        return defaultNumber
    
location = []
location.append([3198, 1030, '', 5, 0])

location2 = []
location2.append([3315, 1067, '', 4, 1])



locationRuns = len(location)

averageTimeStamped = 1
for temp in range(0, locationRuns):
    total = total + 1
    totalTimeStamped = totalTimeStamped + location[temp][4]
    averageTimeStamped = totalTimeStamped/total

total = 0
totalSinceClick = 0
totalTimeStamped = 0    
verbose = 'n'  # input("\nRun program verbosly? (y/n) ")
print("\nPercision for sleep timer:\n0) none  1) 0.90/1.10  2) 0.75/1.25  3) 0.5/1.5")
variance = setNumberInputToDefaultIfNone(input("Choice: "), 0)
while (True == True):
    runs = setNumberInputToDefaultIfNone(input("How many runs: "), 0)
    print("Expected Run Time: " + str(averageTimeStamped*locationRuns*runs))
    for x in range(0, runs):
        for temp in range(0, locationRuns):
            waitTime = location[temp][4]
            totalSinceClick = totalSinceClick + 0.3
            if (random.randint(1, 100) >= (98 - totalSinceClick)):
                totalSinceClick = 0
                modifiedLocation = modifyLocationMove(location2[0][0], location2[0][1], location2[0][3])
                variantSleep(variance, waitTime)
                mouseOutOfRange(modifiedLocation)
                performLeftClick(pyautogui.position())
                
            if (x == 0 and temp == 0):
                waitTime = 0
            startTime = time.time()
            total = total + 1
            timeLeft = round(averageTimeStamped *
                             ((locationRuns*runs)-((x+1)*(temp+1))))
            totalTimeLeft = ("Total Time: " +
                             str(int((timeLeft) // 60)) + ":" +
                             ("0" if ((timeLeft) % 60) < 10 else "") +
                             str(round((timeLeft) % 60, 5)))
            print("\n" + str(location[temp]) + " || " + "Item #" + str(temp+1) + " of " + str(
                locationRuns) + " || loop:" + str(x+1) + " of " + str(runs) + " || " + totalTimeLeft)

            if (location[temp][1] != 0 and location[temp][1] != 0):
                if (random.randint(0, 10) >= 8 and locationRuns > 2):
                    randomlocation = random.randint(0, locationRuns-1)
                    modifyLocationMove(location[randomlocation][0], location[randomlocation][1], 30)

                modifiedLocation = modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                variantSleep(variance, waitTime)
                mouseOutOfRange(modifiedLocation)
                performLeftClick(pyautogui.position())

            if (location[temp][2] != ''):
                sleepRandom(0.5, 0.9)
                if (location[temp][2] == "alttab"):
                    pyautogui.keyDown('alt')
                    sleepRandom(0.1, 0.2)
                    pyautogui.press('tab')
                    sleepRandom(0.1, 0.2)
                    pyautogui.keyUp('alt')
                    pass
                elif (location[temp][2] == 'clickinv'):
                    clickInventory([])
                    pass

                if (verbose.lower() == "y" or verbose.lower() == "yes"):
                    print("Pressing key: " + str(location[temp][2]))

                pyautogui.press(location[temp][2])

            if (waitTime == 0):
                variantSleep(variance, waitTime)
            else:
                variantSleep(variance, 0.5)

            runTimeStamped = (time.time()-startTime)
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Iteration took: " + str(runTimeStamped) + "s")

        print("\nAverage Time Stamped took: " + str(averageTimeStamped) + "s\n")

    print("\n\n----------------------")
    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
