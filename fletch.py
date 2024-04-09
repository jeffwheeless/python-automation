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
        print("Long sleep of: " + str(sleep))
        # if (random.randint(1, 1000) > 950):
        #     sleepRandom(0, 20)
    if (verbose.lower() == "y" or verbose.lower() == "yes"):
        print(sleep)

    time.sleep(sleep)

    if (random.randint(1, 1000) > 950):
        sleepRandom(0, 0.5)
    if (random.randint(1, 1000) > 975):
        sleepRandom(0, 1)
    # if (random.randint(1, 1000) > 995):
    #     sleepRandom(0, 5)
    # if (random.randint(1, 1000) > 990):
    #     print("-- Long Break --")
    #     sleepRandom(1, 15)

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
    
def doClick(side = 'leftClick'):
    if (side != 'rightClick'):
        MouseAutomation.performLeftClick(pyautogui.position())
    else:
        MouseAutomation.performRightClick(pyautogui.position())
        
def prettyTime(seconds, preString = ''):
    return (preString +
             str(int((seconds) // 60)) + ":" +
             ("0" if ((seconds) % 60) < 10 else "") +
             str(round((seconds) % 60, 5)))
    
def runIteration(locations):
    print(locations)
    locationsRuns = len(locations)
    for temp in range(0, locationsRuns):
        waitTime = locations[temp][4]
        # if (x == 0 and temp == 0):
        #     waitTime = 0
        startTimeIteration = time.time()
        timeLeft = round(averageTimeStamped *
                            ((locationsRuns*runs)-((x+1)*(temp+1))))
        totalTimeLeft = prettyTime(timeLeft, "Total Time: ")
        # print("\nTotal:" + str(x+1) + " of " + str(runs) + " || " + str(locations[temp]) + " || " + "Item #" + str(temp+1) + " of " + str(
        #     locationsRuns) + " || " + totalTimeLeft)

        if (locations[temp][1] != 0 and locations[temp][1] != 0):
            if (random.randint(0, 10) >= 8 and locationsRuns > 2):
                randomlocations = random.randint(0, locationsRuns-1)
                if (locations[randomlocations][1] != 0 and locations[randomlocations][1] != 0):
                    MouseAutomation.modifyLocationMove(locations[randomlocations][0], locations[randomlocations][1], 30)
                    
            print(locations[temp])
            if (random.randint(1, 100) < 75):
                variantSleep(variance, waitTime)
                modifiedLocation = MouseAutomation.modifyLocationMove(locations[temp][0], locations[temp][1], locations[temp][3])
            else:
                sleepRandom(0.01, 0.1)
                modifiedLocation = MouseAutomation.modifyLocationMove(locations[temp][0], locations[temp][1], locations[temp][3])
                variantSleep(variance, waitTime)
            sleepRandom(0.01, 0.1)
            MouseAutomation.mouseOutOfRange(modifiedLocation, True)
            doClick(locations[temp][2])
            
            if (waitTime > 2 and random.randint(1, 1000) > 980):
                print("-- Long Break --")
                sleepRandom(5, 120)

        if (locations[temp][2] != ''):
            sleepRandom(0.5, 1.5)
            if (locations[temp][2] == "alttab"):
                pyautogui.keyDown('alt')
                sleepRandom(0.1, 0.2)
                pyautogui.press('tab')
                sleepRandom(0.1, 0.2)
                pyautogui.keyUp('alt')
                pass
            elif (locations[temp][2] == 'clickinv'):
                Inventory.clickInventory([])
                pass

            if (verbose.lower() == "y" or verbose.lower() == "yes"):
                print("Pressing key: " + str(locations[temp][2]))

            pyautogui.press(locations[temp][2])

        # if (waitTime == 0):
        #     variantSleep(variance, waitTime)
        # else:
        #     variantSleep(variance, 0.5)
        
        runTimeStampedIteration = (time.time()-startTimeIteration)
        print("Iteration took: " + str(round(runTimeStampedIteration, 7)) + ' seconds')
        
def runUntilSuccess(image, location):
    pixelMatchColor = pyautogui.pixelMatchesColor(3465, 1045, (0, 255, 192))
    print(pixelMatchColor)
    pix = pyautogui.pixel(3465, 1045)
    print(pix)
    while (pixelMatchColor != True):
        runIteration(location)
        # pictureLocation = pyautogui.locateOnScreen(image, confidence=0.9)
        # pictureLocation = pyautogui.locate(image)
        pixelMatchColor = pyautogui.pixelMatchesColor(3465, 1045, (0, 255, 192))
        print(pixelMatchColor)
        pix = pyautogui.pixel(3465, 1045)
        print(pix)
            
    return True
        
        
    
    
location = []
invLocation = []
inputCheck = input('Click 1')
mousePointer = pyautogui.position()
location.append([mousePointer[0], mousePointer[1], '', 8, 45])
# inputCheck = input('Click 2')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 8, 45])
# inputCheck = input('Click 3')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1]) # knife
# inputCheck = input('Click 4')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '3', 5, 1])
# inputCheck = input('Click 5')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1])
# inputCheck = input('Click 6')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1])
# inputCheck = input('Click 7')
# mousePointer = pyautogui.position()
# location.append([mousePointer[0], mousePointer[1], '', 5, 1])
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
location = [[2872, 460, '', 8, 45], [2576, 742, '', 8, 45]]
items = [[3511, 962, '', 5, 1], [3462, 964, '3', 5, 1]]
invLocations = [
    [[3366, 835, '', 5, 0.5], [3414, 834, '', 5, 0.5], [3465, 837, '', 5, 0.5], [3464, 877, '', 5, 0.5], [3414, 877, '', 5, 0.5], [3365, 877, '', 5, 0.5], [3367, 921, '', 5, 0.5], [3416, 917, '', 5, 0.5], [3463, 920, '', 5, 0.5], [3467, 964, '', 5, 0.5], [3415, 961, '', 5, 0.5], [3366, 960, '', 5, 0.5], [3366, 1002, '', 5, 0.5], [3418, 1003, '', 5, 0.5], [3467, 1001, '', 5, 0.5], [3465, 918, '', 5, 0.5], [3414, 1043, '', 5, 0.5], [3367, 1044, '', 5, 0.5]],
    [[3366, 836, '', 5, 0.5], [3417, 834, '', 5, 0.5], [3415, 880, '', 5, 0.5], [3366, 880, '', 5, 0.5], [3365, 919, '', 5, 0.5], [3422, 923, '', 5, 0.5], [3419, 962, '', 5, 0.5], [3368, 967, '', 5, 0.5], [3368, 1001, '', 5, 0.5], [3421, 1004, '', 5, 0.5], [3414, 1049, '', 5, 0.5], [3368, 1044, '', 5, 0.5], [3466, 1046, '', 5, 0.5], [3467, 1004, '', 5, 0.5], [3467, 957, '', 5, 0.5], [3467, 918, '', 5, 0.5], [3466, 876, '', 5, 0.5], [3460, 837, '', 5, 0.5]],
    [[3370, 1042, '', 5, 0.5], [3421, 1044, '', 5, 0.5], [3467, 1042, '', 5, 0.5], [3467, 999, '', 5, 0.5], [3416, 1001, '', 5, 0.5], [3364, 1001, '', 5, 0.5], [3367, 957, '', 5, 0.5], [3417, 961, '', 5, 0.5], [3467, 962, '', 5, 0.5], [3466, 919, '', 5, 0.5], [3420, 919, '', 5, 0.5], [3365, 914, '', 5, 0.5], [3368, 876, '', 5, 0.5], [3368, 830, '', 5, 0.5], [3423, 837, '', 5, 0.5], [3423, 878, '', 5, 0.5], [3464, 877, '', 5, 0.5], [3464, 835, '', 5, 0.5]],   
]

# print(str(location))
# print(str(invLocations))
# location = [
#     [283, 879, '', 6, 1],
#     [357, 882, 'escape', 5, 1],
#     [528, 847, '', 6, 1],
#     [593, 848, 'space', 7, 1],
#     [626, 1153, '', 7, 32],
#     [746, 1001, '', 7, 1]
# ]

# print(str(location))
# location = [[816, 892, '', 5, 29], [820, 797, '', 5, 29], [1002, 604, '', 5, 29], [627, 131, '', 5, 8]]
# location.append([1645, 592, '', 2, 1])
# location.append([171, 1117, '', 2, 2])
# location.append([587, 979, '', 2, 0])
# location.append([0, 0, 'escape', 1, 0])

print(str(location))

locationRuns = len(location)
invLocationRuns = len(invLocations)

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
    print("\n")
    evenClick = False;
    for x in range(0, runs):
        startTime = time.time()
        total = total + 1
        runUntilSuccess('fullInv.png', location)
        # variantSleep(variance, 60)
        runIteration(items)
        variantSleep(variance, 50)
        randomRun = random.randint(0, len(invLocations)-1)
        invLocation = invLocations[randomRun]
        runIteration(invLocation)
        
        

        runTimeStamped = (time.time()-startTime)
        print("Loop took: " + str(round(runTimeStamped, 7)))
        totalTimeStamped = totalTimeStamped + runTimeStamped
        averageTimeStamped = totalTimeStamped/(total)
        if (runTimeStamped > longestTime):
            longestTime = runTimeStamped
        
        if (runTimeStamped < shortestTime):
            shortestTime = runTimeStamped
                        
            
        print("\nTotal:" + str(x+1) + " of " + str(runs) + " || " + str(invLocation[temp]))

        # print("Average Time Stamped took: " + str(averageTimeStamped) + "s\n")
        if (totalTimeStamped > 0):
            print(
                prettyTime(round(shortestTime,5), "Shortest: ") + " -- " +
                prettyTime(round(averageTimeStamped, 5), "Average: ") + " -- " +
                prettyTime(round(longestTime,5), "Longest: ")
                )

    print("\n\n----------------------")
