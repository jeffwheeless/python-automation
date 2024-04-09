import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

from modules.mouseAutomation import MouseAutomation
from modules.inventory import Inventory

total = 0
totalTimeStamped = 0

def sleepRandom(smallInt, largeInt):
    global verbose
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        # print("Long sleep of: " + str(sleep))
        if (random.randint(1, 1000) > 950):
            sleepRandom(0, 20)
    if (verbose.lower() == "y" or verbose.lower() == "yes"):
        print(sleep)

    time.sleep(sleep)

    if (random.randint(1, 1000) > 825):
        sleepRandom(0, 0.5)
    if (random.randint(1, 1000) > 925):
        sleepRandom(0, 1)

    # if (sleep > 0.5):
    #     if (random.randint(1, 1000) > round(925-largeInt)):
    #         sleepRandom(1, 2)

    #     if (random.randint(1, 1000) > round(960-largeInt)):
    #         sleepRandom(1, 3)

    #     if (random.randint(1, 1000) > round(990-largeInt)):
    #         sleepRandom(1, 20)


def variantSleep(variance, timer):
    if (timer == 0):
        sleepRandom(0.05, 0.1)
    elif (variance == 0):
        # sleepRandom(timer*.98, timer*1.02)
        sleepRandom(timer, timer*1.02)
    elif (variance == 1):
        # sleepRandom(timer*.90, timer*1.1)
        sleepRandom(timer, timer*1.1)
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
            defaultNumber = random.randint(1, 100)
                        
        return defaultNumber
    
oreLocation = []
inputCheck = input('oreLocation Click 1')
ore = pyautogui.position()
oreLocation.append([ore[0], ore[1], '', 5, 1])
inputCheck = input('oreLocation Click 2')
ore = pyautogui.position()
oreLocation.append([ore[0], ore[1], '', 5, 1])
inputCheck = input('oreLocation Click 3')
ore = pyautogui.position()
oreLocation.append([ore[0], ore[1], '', 5, 1])


# location = []
# inputCheck = input('Click 4')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 1])
# inputCheck = input('Click 5')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 9])
# inputCheck = input('Click 6')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 2])

# oreLocation = [[818, 804, '', 6, 1.2], [760, 864, '', 6, 1.2], [816, 918, '', 6, 1]]
location = [[988, 617, '', 6, 1], [780, 893, '', 5, 5], [650, 1037, '', 5, 4]]

print(str(oreLocation))
print(str(location))

locationRuns = len(location)

averageTimeStamped = 1
for temp in range(0, locationRuns):
    total = total + 1
    totalTimeStamped = totalTimeStamped + location[temp][4]
    averageTimeStamped = totalTimeStamped/total

total = 0
totalTimeStamped = 0    
shortestTime = 5000000
longestTime = 0
verbose = 'n'  # input("\nRun program verbosly? (y/n) ")
print("\nPercision for sleep timer:\n0) none  1) 0.90/1.10  2) 0.75/1.25  3) 0.5/1.5")
variance = setNumberInputToDefaultIfNone(input("Choice: "), 0)
singleRunTime = 0
# breakEvent = 
for val in location:
    singleRunTime += val[4]
    
while (True == True):
    runs = setNumberInputToDefaultIfNone(input("How many runs: "), 0)
    print("Expected Run Time: " + str(averageTimeStamped*locationRuns*runs))
    evenClick = False;
    for x in range(0, runs):
        startTime = time.time()
        random.shuffle(oreLocation)
        oreCount = 0
        for bag in range(0, 9):
            if (random.randint(0, 10) >= 8):
                variantSleep(variance, 2)
                random.shuffle(oreLocation)
                
            startTimeIteration = time.time()
            for ore in range(0, 3):
                waitTime = oreLocation[ore][4]
                variantSleep(variance, waitTime)
                modifiedLocation = MouseAutomation.modifyLocationMove(oreLocation[ore][0], oreLocation[ore][1], oreLocation[ore][3])
                MouseAutomation.mouseOutOfRange(modifiedLocation)
                MouseAutomation.performLeftClick(pyautogui.position())
                
                if (random.randint(0, 10) >= 7):
                    MouseAutomation.performLeftClick(pyautogui.position())
            
            
            oreCount = oreCount + 3
            runTimeStampedIteration = (time.time()-startTimeIteration)
            print("Run " + str(x) + " of " + str(runs) + " || Iteration took: || Ore Count: " + str(oreCount))
            variantSleep(variance, 3)
        
        if (random.randint(0, 10) >= 5):
            variantSleep(variance, waitTime)
            modifiedLocation = MouseAutomation.modifyLocationMove(oreLocation[0][0], oreLocation[0][1], oreLocation[0][3])
            MouseAutomation.mouseOutOfRange(modifiedLocation)
            MouseAutomation.performLeftClick(pyautogui.position())
        
        
        # breakTimeClock = 
        # if ((singleRunTime * runs) > 440):
            # variantSleep(variance, waitTime/2)
            
        for temp in range(0, locationRuns):
            if (random.randint(1, 1000) > 995):
                print("-- Long Break --")
                sleepRandom(5, 60)
                
                
            waitTime = location[temp][4]
            if (x == 0 and temp == 0):
                waitTime = 0
            startTimeIteration = time.time()
            total = total + 1
            timeLeft = round(averageTimeStamped *
                             ((locationRuns*runs)-((x+1)*(temp+1))))
            totalTimeLeft = ("Total Time: " +
                             str(int((timeLeft) // 60)) + ":" +
                             ("0" if ((timeLeft) % 60) < 10 else "") +
                             str(round((timeLeft) % 60, 5)))
            # print("\nTotal:" + str(x+1) + " of " + str(runs) + " || " + str(location[temp]) + " || " + "Item #" + str(temp+1) + " of " + str(
            #     locationRuns) + " || " + totalTimeLeft)

            if (location[temp][1] != 0 and location[temp][1] != 0):
                if (random.randint(0, 10) >= 8 and locationRuns > 2):
                    randomlocation = random.randint(0, locationRuns-1)
                    MouseAutomation.modifyLocationMove(location[randomlocation][0], location[randomlocation][1], 30)

                variantSleep(variance, waitTime)
                modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                MouseAutomation.mouseOutOfRange(modifiedLocation)
                MouseAutomation.performLeftClick(pyautogui.position())
                
                # if (random.randint(1, 1000) > 250 and evenClick == True):
                #     evenClick = False;
                #     variantSleep(variance, waitTime/2)
                #     # MouseAutomation.mouseOutOfRange(modifiedLocation)
                #     MouseAutomation.performLeftClick(pyautogui.position())
                
                # if (random.randint(1, 1000) > 910 and evenClick == False):
                #     evenClick = True;
                #     variantSleep(variance, waitTime/2)
                #     # MouseAutomation.mouseOutOfRange(modifiedLocation)
                #     MouseAutomation.performLeftClick(pyautogui.position())

            if (location[temp][2] != ''):
                sleepRandom(0.5, 1.5)
                if (location[temp][2] == "alttab"):
                    pyautogui.keyDown('alt')
                    sleepRandom(0.1, 0.2)
                    pyautogui.press('tab')
                    sleepRandom(0.1, 0.2)
                    pyautogui.keyUp('alt')
                    pass
                elif (location[temp][2] == 'clickinv'):
                    Inventory.clickInventory([])
                    pass

                if (verbose.lower() == "y" or verbose.lower() == "yes"):
                    print("Pressing key: " + str(location[temp][2]))

                pyautogui.press(location[temp][2])

            # if (waitTime == 0):
            #     variantSleep(variance, waitTime)
            # else:
            #     variantSleep(variance, 0.5)
            
            runTimeStampedIteration = (time.time()-startTimeIteration)
            print("Iteration took: " + str(round(runTimeStampedIteration, 7)))
        
        variantSleep(variance, 5)

        if (x > 1):
            runTimeStamped = (time.time()-startTime)
            print("Loop took: " + str(round(runTimeStamped, 7)))
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/(total-1)
            if (runTimeStamped > longestTime):
                longestTime = runTimeStamped
            
            if (runTimeStamped < shortestTime):
                shortestTime = runTimeStamped
                    
        
        print("\nTotal:" + str(x+1) + " of " + str(runs) + " || " + str(location[temp]) + " || " + totalTimeLeft)

        # print("Average Time Stamped took: " + str(averageTimeStamped) + "s\n")
        if (totalTimeStamped > 0):
            print("Shortest: " + str(round(shortestTime,5)) + " --  Average: " + str(round(averageTimeStamped, 5)) + " -- Longest: " + str(round(longestTime,5)))
        
        

    print("\n\n----------------------")
