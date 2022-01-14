
import time
from datetime import datetime
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
latestDaysHour = 0
earliestDaysHour = 6


def performLeftClick(mainLocation, repeatedWord=""):
    global dryRun
    mainLocation = mouseOutOfRange(mainLocation)
    if (dryRun == False):
        sleep = round(random.uniform(0, 1), 10)
        time.sleep(sleep)
        print("Clicking")
        pyautogui.leftClick(
            mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
        if (repeatedWord != ""):
            if (random.randint(1, 10) > 7):
                badCommand(repeatedWord)
            print("Giving command: " + repeatedWord)
            writeSleepEnter(repeatedWord)


def badCommand(currentCommand):
    sleep = round(random.uniform(0, 1), 10)
    fastActions = ['bank', 'm stats']
    slowActions = ['q', 'mine coal', 'fish swordfish', 'laps Canifis Rooftop Course', 'chop logs']
    if (random.randint(1, 100) > 75):
        writeSleepEnter(fastActions[random.randint(0, int(len(fastActions)))])
    elif (random.randint(1, 100) > 75):
        writeSleepEnter(slowActions[random.randint(0, int(len(slowActions)))])
        sleepRandom(33*60, 37*60)
    elif (random.randint(1, 100) > 75):
        writeSleepEnter(currentCommand)
        sleepRandom(33*60, 37*60)
    sleepRandom(2, 4)


def writeSleepEnter(typedString):
    pyautogui.write("+" + typedString)
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('enter')


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    totalTime = totalTime + sleep
    # sleep = 60 + sleep
    # print(sleep)
    if (dryRun == False):
        print(formatHumanTimeString(sleep))
        time.sleep(0.3) # time.sleep(sleep)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+7 or current[0] <= mainLoc[0]-7):
        # foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            mainLoc[0] + random.randint(-5, 5),
            mainLoc[1] + random.randint(-5, 5),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6) - (0.3/2),
            random.uniform(0.6, 0.8) + (0.3/2)
        )
        current = pyautogui.position()

    return current


def performClick(current, mainLocation, repeatedWord=""):

    global latestDaysHour
    global earliestDaysHour
    now = datetime.now()
    current_time_hour = int(datetime.now().strftime("%H"))
    smallTime = random.uniform(32*60, 32.5*60)
    largeTime = random.uniform(32.6*60, 35*60)
    if (current_time_hour >= earliestDaysHour and current_time_hour < latestDaysHour):
        print("slow")
        smallTime = random.uniform(30*60, 60*60)
        largeTime = random.uniform(70*60, 200*60)

    if (current_time_hour < earliestDaysHour or current_time_hour >= latestDaysHour):
        print("fast")
        if (random.randint(1, 10) > 9):
            largeTime = random.uniform(34.1*60, 39.9*60)
        elif (random.randint(1, 10) > 9):
            largeTime = random.uniform(36*60, 42*60)

    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation, repeatedWord)
    sleepRandom(smallTime, largeTime)


def formatHumanTimeString(seconds):
    timeLeftMin = round((seconds) // 60)
    timeLeftSec = ("0" if ((seconds) % 60) <
                   10 else "") + str(round(seconds % 60, 5))
    return str(timeLeftMin) + ":" + str(timeLeftSec)


def clickLocations(mainLocation, repeatedWords, iterations, wordCount):
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == False):
            print("\n============ Run: " + str(i + 1) +
                  " of " + str(iterations) + " ============")
            timeLeft = formatHumanTimeString(
                averageTime * (iterations - i))
            print("==== Time Left: " + str(timeLeft) + " ====")

        for word in range(0, wordCount):
            if (dryRun == True):
                total = total + 1
                performClick(pyautogui.position(), mainLocation)
            elif (dryRun == False):
                mainLocation = mouseOutOfRange(mainLocation)
                current = pyautogui.position()
                random.shuffle(repeatedWords)
                performClick(current, mainLocation, repeatedWords[word])
    return True


def run(mainLocation, repeatedWords, iterations, wordCount):
    return clickLocations(mainLocation, repeatedWords, iterations, wordCount)


while True == True:
    repeatedWords = [
        "sell 55 Bronze bolts", 
        "sell 14 Bronze arrow", 
        "sell 273 Bronze platebody", 
        "sell 5 Bronze spear", 
        "sell 1 Bronze axe", 
        "sell 4 Bronze bar", 
        "sell 10 Dwarven stout", 
        "sell 2 Cabbage", 
        "sell 1 Iron full helm", 
        "sell 167 Iron platebody", 
        "sell 3 Iron sword", 
        "sell 8 Purple firelighter", 
        "sell 2 Black bead", 
        "sell 3 Red bead", 
        "sell 6 White bead", 
        "sell 5 Yellow bead",
    ]
    wordCount = len(repeatedWords)
    iterations = int(round(720 / (int(wordCount) * 30), 0))

    if (type(iterations) == str):
        iterations = int(iterations)
    if (iterations <= 0):
        iterations = 140

    mainLocation = pyautogui.position()
    dryRun = True
    dryRunItemCount = 50
    success = clickLocations(
        mainLocation, repeatedWords[0], dryRunItemCount, 1)
    averageTime = totalTime/total
    averageTimeLeftStr = formatHumanTimeString(totalTime/total)
    print("\n\nAverage Time: " + str(averageTimeLeftStr))
    dryRun = False
    # performLeftClick(mainLocation, repeatedWords)
    running = run(mainLocation, repeatedWords, iterations, int(wordCount))
    print("\nTotal Time: " + formatHumanTimeString((iterations*averageTime)))
    quit()
