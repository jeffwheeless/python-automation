
import time
from datetime import datetime
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re


def findIt(pattern, word):
    results = pattern.search(word)
    if (results == None):
        print("not found")
    elif (results.group(0) != None):
        wordTwoSplit = re.split(pattern, word)
        print(results.group(0) + wordTwoSplit[1])


while True == True:
    wordOne = '+bf mithril bar'
    wordTwo = '/k barrows'
    pattern = re.compile("/[A-z]+")
    # findIt(pattern, wordOne)
    findIt(pattern, wordTwo)

    # wordCount = len(repeatedWords)
    # print(wordCount)
    # iterations = int(round(720 / (int(wordCount) * 30), 0))
    # print(iterations)
    # # quit()
    # for foo in range(0, iterations+5000):
    #     if (type(iterations) == str):
    #         iterations = int(iterations)
    #     if (iterations <= 0):
    #         iterations = 140

    #     mainLocation = pyautogui.position()
    #     dryRun = True
    #     dryRunItemCount = 50
    #     success = clickLocations(
    #         mainLocation, repeatedWords[0], dryRunItemCount, 1)
    #     averageTime = totalTime/total
    #     averageTimeLeftStr = formatHumanTimeString(totalTime/total)
    #     print("\n\nAverage Time: " + str(averageTimeLeftStr))
    #     dryRun = False
    #     # sleepRandom(32*60, 40*60)
    #     running = run(mainLocation, repeatedWords, iterations, int(wordCount))
    #     print("\nTotal Time: " + formatHumanTimeString((iterations*averageTime)))
    quit()
