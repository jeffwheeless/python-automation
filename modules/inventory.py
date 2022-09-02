import pyautogui
import random
import time
import time
from mouseAutomation import *
import json

import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/modules')
import configHelper
import mouseAutomation


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    # if (verbose.lower() == "y" or verbose.lower() == "yes"):
    #     print(sleep)

    time.sleep(sleep)
    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 0.5)

    # if (random.randint(1, 1000) > 925):
    #     sleepRandom(1, 2)

    # if (random.randint(1, 1000) > 960):
    #     sleepRandom(1, 3)


def clickInventory(skipItemNumberArray=[]):
    config = configHelper.read_config()
    invLocs = []
    inventoryLocsConfig = config.items('InventoryLocs')
    for temp in range(0, 28):
        invLocs.append([json.loads(inventoryLocsConfig[temp][1])[0],
                        json.loads(inventoryLocsConfig[temp][1])[1]])

    # skipItemNumberArray = []
    # skips = int(input("How many locations to skip: "))
    # for temp in range(0, skips):
    #     skipItemNumber = int(
    #         input("Item to skip " + str(temp+1) + " of " + str(skips) + ": ")) - 1
    #     skipItemNumberArray.append(skipItemNumber)

    inventoryPatterns = [
        # straight lines
        ['1', '2', '3', '4', '8', '7', '6', '5', '9', '10', '11', '12', '16', '15',
         '14', '13', '17', '18', '19', '20', '24', '23', '22', '21', '25', '26', '27', '28'],
        # 1 straight lines then double columns
        ['1', '2', '6', '5', '9', '10', '14', '13', '17', '18', '22', '21', '25',
         '26', '27', '28', '24', '23', '19', '20', '16', '15', '11', '12', '8', '7', '3', '4'],
        # 2 straight lines then double columns
        ['1', '2', '3', '4', '8', '7', '6', '5', '9', '10', '14', '13', '17', '18',
         '22', '21', '25', '26', '27', '28', '24', '23', '19', '20', '16', '15', '11', '12']
    ]

    inventoryPattern = inventoryPatterns[random.randint(0, 2)]
    locationRuns = len(inventoryPattern)
    for temp in range(0, locationRuns):
        invLocation = int(inventoryPattern[temp])-1
        if (invLocation not in skipItemNumberArray):
            modloc = [
                random.randint(int(invLocs[invLocation][0])-5,
                               int(invLocs[invLocation][0])+5),
                random.randint(int(invLocs[invLocation][1])-5,
                               int(invLocs[invLocation][1])+5),
            ]

            if (random.randint(0, 1) == 0):
                current = pyautogui.position()
                mouseMove(current[0], current[1], modloc[0], modloc[1])
                sleepRandom(0.01, 0.05)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())
            else:
                sleepRandom(0.01, 0.05)
                current = pyautogui.position()
                mouseMove(current[0], current[1], modloc[0], modloc[1])
                # sleepRandom(0.01, 0.05)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())

            sleepRandom(0.01, 0.05)
