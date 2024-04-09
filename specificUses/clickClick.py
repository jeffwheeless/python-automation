import datetime
import time
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re
import os

def clickLocations(mainLocation, iterations):
    global total, averageTime
    global dryRun
    global runTimeStamped
    global totalTimeStamped
    global averageTimeStamped
    global longestRun
    global shortestRun
    # pyautogui.press('escape')
    for i in range(0, iterations):
        print("Run " + str(i) + " of " + str(iterations))
        pyautogui.leftClick(mainLocation[0], mainLocation[1], random.uniform(0.001, 0.1))

while True == True:
    # run(mainLocation, item, pixelColorItem, itemCount)
    input2 = input("Left Click? ")
    # itemCount = 127 #input("Hover over item location, how many are there? ")
    itemCount = input2 #input("Hover over item location, how many are there? ")
    if (itemCount == "" or itemCount == "0"):
        itemCount = random.randint(15, 200)
    if (type(itemCount) == str):
        itemCount = int(itemCount)

    mainLocation = pyautogui.position()
    clickLocations(mainLocation, itemCount)
    