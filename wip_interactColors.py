import datetime
import time
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re
import os


from modules.mouseAutomation import MouseAutomation
from modules.inventory import Inventory

total = 0
totalTimeStamped = 0
verbose = 'n'

def sleepRandom(smallInt, largeInt):
    global verbose
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))
    if (verbose.lower() == "y" or verbose.lower() == "yes"):
        print(sleep)

    time.sleep(sleep)

    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 0.5)

    # if (sleep > 0.5):
    #     if (random.randint(1, 1000) > round(925-largeInt)):
    #         sleepRandom(1, 2)

    #     if (random.randint(1, 1000) > round(960-largeInt)):
    #         sleepRandom(1, 3)

    #     if (random.randint(1, 1000) > round(990-largeInt)):
    #         sleepRandom(1, 20)

# item = pyautogui.position()
# frameinfo = getframeinfo(currentframe())
# fileName = re.sub(r'[^A-z]', r'', str(frameinfo.filename))
# dt = datetime.datetime.now()
# dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
# pixelColorItem = pyautogui.screenshot(
#     imageFilename=".screenshot" +
#     str(fileName) + str(frameinfo.lineno) + ".png",
#     region=(item[0], item[1], 10, 10)
# ).getcolors()
def clickPicture(pictureLocation):
    # print(str(pictureLocation[0]))
    current = pyautogui.position()
    location = [
        round(pictureLocation[0] + (pictureLocation[2]/2)),
        round(pictureLocation[1] + (pictureLocation[3]/2)),
        5
    ]
    modifiedLocation = MouseAutomation.modifyLocationMove(location[0], location[1], 5)
    # MouseAutomation.mouseOutOfRange(modifiedLocation)
    # MouseAutomation.mouseMove(modifiedLocation)
    # pyautogui.moveTo(location[0], location[1])
    sleepRandom(0.1, 0.2)
    pyautogui.leftClick(modifiedLocation[0], modifiedLocation[1])
    sleepRandom(0.1, 0.2)
    # MouseAutomation.performLeftClick(pyautogui.position())
    MouseAutomation.modifyLocationMove(current[0], current[1], 15)

while (True == True):
    pictureLocation = pyautogui.locateOnScreen('bigBones.png', confidence=0.9)
    # pictureLocation = pyautogui.locateOnScreen('bone2.png', confidence=0.7)
    print(str(pictureLocation))
    if (pictureLocation != None):
        clickPicture(pictureLocation)
    else:
        pictureLocation = pyautogui.locateOnScreen('smallBones.png', confidence=0.9)
        if (pictureLocation != None):
            clickPicture(pictureLocation)
    sleepRandom(1, 5)