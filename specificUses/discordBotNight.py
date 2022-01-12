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
            if (random.randint(1, 10) > 9):
                badCommand()
            print("Giving command: " + repeatedWord)
            writeSleepEnter(repeatedWord)


def badCommand():
    sleep = round(random.uniform(0, 1), 10)
    if (random.randint(1, 10) > 8):
        if (random.randint(1, 10) > 9):
            writeSleepEnter("+bak")
        if (random.randint(1, 10) > 9):
            writeSleepEnter("+bnak")
        writeSleepEnter("+bank")
    elif (random.randint(1, 10) > 7):
        writeSleepEnter("+m stats")
    sleepRandom(2, 4)


def writeSleepEnter(typedString):
    pyautogui.write(typedString)
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
        time.sleep(sleep)


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
    smallTime = random.uniform(50*60, 60*60)
    largeTime = random.uniform(90.6*60, 200*60)
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
        for word in range(0, wordCount):
            if (dryRun == True):
                total = total + 1
                performClick(pyautogui.position(), mainLocation)
            elif (dryRun == False):
                print("\n============ Run: " + str(i + 1) +
                      " of " + str(iterations) + " ============")
                timeLeft = formatHumanTimeString(
                    averageTime * (iterations - i))
                print("==== Time Left: " + str(timeLeft) + " ====")
                mainLocation = mouseOutOfRange(mainLocation)
                current = pyautogui.position()
                performClick(current, mainLocation, repeatedWords[word])
    return True


def run(mainLocation, repeatedWords, iterations, wordCount):
    return clickLocations(mainLocation, repeatedWords, iterations, wordCount)


while True == True:
    # run(mainLocation, item, itemCount)
    # iterations = 2
    wordCount = input("How many commands ")
    iterations = int(round(720 / (int(wordCount) * 30), 0))
    repeatedWord = input("Repeat what command? ")
    repeatedWords = [repeatedWord]

    for x in range(0, int(wordCount)-1):
        print("Run number " + str(x))
        repeatedWord = input("Repeat what command? ")
        repeatedWords.append(repeatedWord)

    if (type(iterations) == str):
        iterations = int(iterations)
    if (iterations <= 0):
        iterations = 140

    # intention is to make two diff locations and mouse move
    mainLocation = pyautogui.position()
    dryRun = True
    dryRunItemCount = 50
    # if (itemCount < 100):
    #     dryRunItemCount = itemCount*10
    success = clickLocations(
        mainLocation, repeatedWord, dryRunItemCount, 1)
    averageTime = totalTime/total
    averageTimeLeftStr = formatHumanTimeString(totalTime/total)
    print("\n\nAverage Time: " + str(averageTimeLeftStr))
    dryRun = False
    # performLeftClick(mainLocation, repeatedWords)
    running = run(mainLocation, repeatedWords, iterations, int(wordCount))
    print("\nTotal Time: " + formatHumanTimeString((iterations*averageTime)))
