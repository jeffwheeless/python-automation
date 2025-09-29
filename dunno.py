"""
dunno.py - Example of a deliberately inefficient, undetectable automation bot.

This script demonstrates the core philosophy of the project: to automate tasks in a way that is intentionally messy, slow, and unpredictable, making it hard for bot detectors to flag the behavior as automated.

Functions are documented, and logic is commented to clarify the "dumb" design choices.
"""

import time
import random
import pyautogui

# useless, but should turn off if the program clicks or not
# useless because timestamp functions dont operate properly without waits
dryRun = True

# Timestamp for when the iteration first began
startTime = 0

# 
totalTime = 0.0

# Average 
averageTime = 0.0

# Total that is reset with reset variance, aka youre active in paying attention again
newTotal = 0

# Overall total of how many times the program has run since it being was first opened
total = 0
# total = 806

# Time passed since first iteration of a loop
runTimeStamped = 0

# Total time spent with the program running
totalTimeStamped = 0
# totalTimeStamped = 5119.571706533432

# Longest run thus far since running program
longestRun = 0
# longestRun = 149.90719413757324

# Shortest run this far since running program
shortestRun = 100
# shortestRun = 0.8448443412780762

# Time passed since program started per iteation
averageTimeStamped = 6.351825938627087

# Change over time to be reset randomly. aka tiring of doing the action so you go slower
variance = 0

# modify the chances for breaks so each session between breaks is unique-ish
attentive = 0

# Reset with variance, aka im paying attention and therefore not distracted for this long
quickClick = 0

# How deeply nested within a recurise function is the program, used within sleep to stop crazy nesting
depth = 0


def performLeftClick(mainLocation):
    """
    Perform a left mouse click at the specified location.

    Args:
        mainLocation (tuple): The x, y coordinates where the click should occur.
    """
    global dryRun
    if (dryRun == False):
        print("Clicking at " + str(mainLocation))
        # sleepRandom(0.3, 0.7)  # remove if clicking
        pyautogui.leftClick(None, None, 0, random.uniform(0.2, 0.6))


def sleepRandom(smallInt, largeInt):
    """
    Sleep for a random duration between smallInt and largeInt.

    Args:
        smallInt (float): The minimum duration to sleep.
        largeInt (float): The maximum duration to sleep.
    """
    global totalTime
    global dryRun
    global variance
    # global startTime
    global depth
    global attentive
    depth = depth + 1
    # global altWindowXY
    smallVarient = smallInt
    largeVarient = largeInt
    if (variance > 0):
        smallVarient = (smallInt*variance)
        # print("Small " + str(smallVarient))
        largeVarient = (largeInt+(largeInt*variance))
    if (largeVarient > 150):
        largeVarient = random.uniform(150, 210)
    # print("large " + str(largeVarient))
    sleep = round(
        random.uniform(
            smallVarient,
            largeVarient
        ),
        10
    )
    # print(sleep)
    
    # afkTime = (time.time()-startTime)
    # print("afkTime: " + str(afkTime))

    # if (afkTime <= random.randint(200, 270)):
    if (depth <= 20):
        if (random.randint(1, 1000) > (734 - attentive)): 
        # if (random.randint(1, 1000) > (730 - attentive)):  #6s - 500 c/h
        # if (random.randint(1, 1000) > (735 - attentive)): #7.5s - 445 c/h
            # sleep = sleep + round(random.uniform(0, 0.4), 10)
            sleepRandom(0, 0.8)

        afkTime = (time.time()-startTime)
        if (variance > 0 and (afkTime+sleep) <= random.randint(260, 300)):
            if (random.randint(1, 1000) > (874 - attentive)):
            # if (random.randint(1, 1000) > (863 - attentive)):  #6s - 500 c/h
            # if (random.randint(1, 1000) > (863 - attentive)): #7.5s - 445 c/h
                sleepRandom(1, 2)
            elif (random.randint(1, 1000) > (924 - attentive)):  
            # elif (random.randint(1, 1000) > (918 - attentive)):  #6s - 500 c/h
            # elif (random.randint(1, 1000) > (918 - attentive)): #7.5s - 445 c/h
                sleepRandom(1, 3)

            if (random.uniform(1, 100) > ((99.35 - (attentive/10)) - variance)): 
            # if (random.uniform(1, 100) > ((99.30 - (attentive/10)) - variance)):  #6s - 500 c/h
            # if (random.uniform(1, 100) > ((99.30 - (attentive/10)) - variance)): #7.5s - 445 c/h
                sleepRandom(0, random.randint(10, 60))
                if (depth <= 2 and random.randint(1, 1000) > 825):
                    distract()
            elif (random.uniform(1, 100) > ((100.60 - (attentive/10)) - variance)): 
            # elif (random.uniform(1, 100) > ((100.55 - (attentive/10)) - variance)): #6s - 500 c/h
            # elif (random.uniform(1, 100) > ((100.55 - (attentive/10)) - variance)): #7.5s - 445 c/h
                variance = variance + 10
                sleepRandom(random.randint(1, 10), 100)
                # distract is triggering from deep calls to this and making it happen too often
                if (depth <= 2 and random.randint(1, 1000) > (815 - variance)): 
                # if (depth <= 2 and random.randint(1, 1000) > (770 - variance)):  #6s - 500 c/h
                # if (depth <= 2 and random.randint(1, 1000) > (825 - variance)): #7.5s - 445 c/h
                    distract()
            
            if (random.randint(1, 1000) > 913):  
            # if (random.randint(1, 1000) > 917):  #6s - 500 c/h
            # if (random.randint(1, 1000) > 909): #7.5s - 445 c/h
                distract()
    else:
        print("Too Deeply Nested")
    
    goToSleep(sleep)
            
def goToSleep(sleepTimer):
    """
    Sleep for a random duration based on sleepTimer.
    This function is intentionally left incomplete to mimic human forgetfulness.
    """
    pass


def mouseOutOfRange(mainLoc):
    """
    Move the mouse to a random location out of the main area.
    This is a stub for anti-detection randomness.

    Args:
        mainLoc (tuple): The current x, y coordinates of the mouse.

    Returns:
        tuple: The (potentially) new x, y coordinates for the mouse.
    """
    return mainLoc


def performActionClick(current, mainLocation, waitTime=3):
    """
    Perform a left click at mainLocation after a random sleep.
    Occasionally does nothing, to simulate human distraction.

    Args:
        current (tuple): The current x, y coordinates of the mouse.
        mainLocation (tuple): The target x, y coordinates for the click.
        waitTime (int, optional): A base time to wait before clicking. Defaults to 3.
    """
    sleepRandom(
        (waitTime + random.uniform(2.8, 3.5)),
        (waitTime + random.uniform(4.5, 4.7))
    )
    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation)
    if random.randint(1, 1000) > 990:
        # Simulate a rare missed click
        pass


def performActionKey(key, mainLocation, waitTime=3):
    """
    Press a key after a random sleep, with mouse moved out of range.

    Args:
        key (str): The key to be pressed.
        mainLocation (tuple): The x, y coordinates (not used in this function).
        waitTime (int, optional): A base time to wait before pressing the key. Defaults to 3.
    """
    sleepRandom(
        (waitTime + random.uniform(2.8, 3.5)),
        (waitTime + random.uniform(4.5, 4.7))
    )
    mainLocation = mouseOutOfRange(mainLocation)
    pyautogui.press(str(key))


def formatTimeLeft(timeLeft):
    """
    Format time left for display. Returns unchanged for now.

    Args:
        timeLeft (float): The time left in seconds.

    Returns:
        The formatted time left.
    """
    # timeLeft = float(timeLeft)
    if timeLeft > 60:
        pass
    else:
        pass
    return timeLeft


def distract():
    """
    Occasionally introduce a long random pause to simulate human distraction.
    """
    global variance, quickClick, attentive
    global newTotal
    global totalTime
    global newTotal
    print("quickClick: " + str(quickClick))
    if quickClick > 45 and random.uniform(1, 100) > (92.9 - variance):
        attentive = random.randint(-5, 6)
        print("Distracted")
        sleepRandom(
            random.randint(30, 45),
            random.randint(100, 240)
        )
        print("Attentive: " + str(attentive))
        print("Locking In")
        variance = 0
        totalTime = 0
        newTotal = 1
        quickClick = 0
    if quickClick < random.randint(random.randint(20, 26), 45):
        print("Quick Clicking")
        variance = 0
        quickClick = quickClick + 1
    else:
        quickClick = 50


def clickLocations(locations, iterations):
    """
    Click through a list of locations for a number of iterations, tracking timing stats.
    Many global variables are used for stats and randomness.

    Args:
        locations (list): A list of locations to click on.
        iterations (int): The number of iterations to perform.
    """
    global startTime
    global total, averageTime
    global dryRun
    global runTimeStamped, totalTimeStamped, averageTimeStamped
    global longestRun, shortestRun
    global totalTime, newTotal
    global variance, quickClick, attentive
    global depth
    for _ in range(0, iterations):
        for loc in locations:
            newTotal = newTotal + 1
            startTime = time.time()
            if quickClick > 45:
                pass
            if False == True and dryRun == True:
                pass
            elif dryRun == False:
                if loc[0] == 0 and loc[1] == 0:
                    pass
                else:
                    pass
            runTimeStamped = (time.time() - startTime)
            if runTimeStamped > longestRun:
                longestRun = runTimeStamped
            if runTimeStamped < shortestRun:
                shortestRun = runTimeStamped
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped / total
            print("\nIteration took: " + str(runTimeStamped) + "s")
            print("Range " + str(shortestRun) + " thru " + str(longestRun))
            print("AverageTimeStamped = TotalTimeStamped  / Total")
            print(str(averageTimeStamped) + " = " +
                  str(totalTimeStamped) + " / " + str(total))
            totalTime = totalTime + runTimeStamped
            print(str((totalTime) / newTotal))
            print(str((totalTime) / newTotal) + " = " +
                  str(totalTime) + " / " + str(newTotal))
    return True


def run(mainLocation, itemCount):
    """
    Run the clickLocations routine with the given locations and item count.

    Args:
        mainLocation (tuple): The x, y coordinates of the main location.
        itemCount (int): The number of items to process.

    Returns:
        The result of the clickLocations function.
    """
    return clickLocations(mainLocation, itemCount)


locations = [
    [1890, 721, "", 0.9122617244720459],
    [1899, 632, "", 1.034623146057129],
    [0, 0, "space", 14.5885329246521]
]

while True:
    itemCount = input("Hover over item location, how many are there (hours)? ")
    if itemCount == "" or itemCount == "0":
        itemCount = random.randint(250, 999)
    if type(itemCount) == str:
        itemCount = int(itemCount)
    mainLocation = pyautogui.position()
    dryRun = True
    dryRunItemCount = 1000
    print("Running dry run test to assess total time")
    dryRun = False
    print("Spell" + str(mainLocation))
    running = run(locations, itemCount)
