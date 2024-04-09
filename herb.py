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

    if (random.randint(1, 1000) > 800):
        sleepRandom(0, 0.5)
    if (random.randint(1, 1000) > 950):
        sleepRandom(0, 1)
    if (random.randint(1, 1000) > 975):
        sleepRandom(0, 5)
    if (largeInt > 15 and random.randint(1, 1000) > 990):
        print("-- Long Break --")
        sleepRandom(5, 60)

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
            defaultNumber = random.randint(1, 100)
                        
        return defaultNumber
    
location = []
# sleep move click press
# inputCheck = input('Click 1')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 12])
# inputCheck = input('Click 2')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], 'escape', 5, 1.5])
# inputCheck = input('Click 3')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1])
# inputCheck = input('Click 4')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], 'space', 5, 1])
# inputCheck = input('Click 5')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1])
# inputCheck = input('Click 6')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 37])
# inputCheck = input('Click 6')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 1])
# inputCheck = input('Click 7')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], 'escape', 5, 2])
# inputCheck = input('Click 8')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 2])
# inputCheck = input('Click 9')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], 'space', 7, 10])
# inputCheck = input('Click 10')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 2])
# inputCheck = input('Click 11')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 7, 2])
print(str(location))
# location = [
#     [283, 879, '', 6, 1],
#     [357, 882, 'escape', 5, 1],
#     [528, 847, '', 6, 1],
#     [593, 848, 'space', 7, 1],
#     [626, 1153, '', 7, 32],
#     [746, 1001, '', 7, 1]
# ]

# location = [[3078, 640, '', 8, 6], [2891, 818, '', 5, 1.5], [2856, 595, '', 5, 1], [2853, 670, 'escape', 5, 1], [3234, 712, '', 5, 1], [3313, 926, '', 5, 15], [3401, 929, 'space', 7, 1]]
location = [[2813, 661, 'escape', 5, 1], [2901, 531, '', 5, 1.5], [3174, 673, '', 8, 30], [2840, 962, '', 5, 1]] #clean them
# location = [[2754, 662, '', 5, 1], [2813, 661, 'escape', 5, 1], [2954, 662, '', 5, 1.5], [3007, 665, 'space', 5, 1], [3174, 673, '', 8, 8], [2840, 962, '', 5, 1]]
# location.append([1645, 592, '', 2, 1])
# location.append([171, 1117, '', 2, 2])
# location.append([587, 979, '', 2, 0])
# location.append([0, 0, 'escape', 1, 0])

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
        total = total + 1
        
        # breakTimeClock = 
        # if ((singleRunTime * runs) > 440):
            # variantSleep(variance, waitTime/2)
            
        for temp in range(0, locationRuns):
            waitTime = location[temp][4]
            if (x == 0 and temp == 0):
                waitTime = 0
            startTimeIteration = time.time()
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
                    if (location[randomlocation][1] != 0 and location[randomlocation][1] != 0):
                        MouseAutomation.modifyLocationMove(location[randomlocation][0], location[randomlocation][1], 30)
                        
                if (random.randint(1, 100) < 75):
                    variantSleep(variance, waitTime)
                    modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                else:
                    sleepRandom(0.01, 0.1)
                    modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                    variantSleep(variance, waitTime)

                variantSleep(variance, waitTime)
                modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                MouseAutomation.mouseOutOfRange(modifiedLocation)
                MouseAutomation.performLeftClick(pyautogui.position())
                
                # if (temp == 0):
                #     variantSleep(variance, waitTime)
                #     # modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                #     MouseAutomation.mouseOutOfRange(pyautogui.position())
                #     MouseAutomation.performLeftClick(pyautogui.position())
                    
                
                # if (random.randint(1, 1000) > 900):
                #     variantSleep(variance, waitTime)
                #     modifiedLocation = MouseAutomation.modifyLocationMove(location[temp][0], location[temp][1], location[temp][3])
                #     MouseAutomation.mouseOutOfRange(modifiedLocation)
                #     MouseAutomation.performLeftClick(pyautogui.position())
                #     evenClick = False;
                #     variantSleep(variance, waitTime/2)
                #     # MouseAutomation.mouseOutOfRange(modifiedLocation)
                #     MouseAutomation.performLeftClick(pyautogui.position())
                # else:
                #     sleep = random.uniform(0.5, 4)
                #     time.sleep(sleep)
                #     MouseAutomation.performLeftClick(pyautogui.position())
                
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
                sleepRandom(1.5, 2.5)
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

        runTimeStamped = (time.time()-startTime)
        print("Loop took: " + str(round(runTimeStamped, 7)))
        totalTimeStamped = totalTimeStamped + runTimeStamped
        averageTimeStamped = totalTimeStamped/(total)
        if (runTimeStamped > longestTime):
            longestTime = runTimeStamped
        
        if (runTimeStamped < shortestTime):
            shortestTime = runTimeStamped
                    
        
        print("\nTotal:" + str(x+1) + " of " + str(runs) + " || " + str(location[temp]) + " || " + totalTimeLeft)

        # print("Average Time Stamped took: " + str(averageTimeStamped) + "s\n")
        if (totalTimeStamped > 0):
            print("Shortest: " + str(round(shortestTime,5)) + " --  Average: " + str(round(averageTimeStamped, 5)) + " -- Longest: " + str(round(longestTime,5)))

    print("\n\n----------------------")
