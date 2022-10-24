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
    # print(sleep)

    time.sleep(sleep)

    # if (random.randint(1, 1000) > 900):
    #     sleepRandom(0, 0.5)

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
def clickPicture(pictureLocation, pictureName):
    # print(str(pictureLocation[0]))
    if (pictureLocation != None):
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
        return True

    return False
    
def clickPictures(images, index):
    if (len(images) == index):
        return False
    
    current = pyautogui.position()
    imageIndex = 0
    if (len(images) > 1):
        imageIndex = random.randint(0, len(images[index])-1)
    print(str(images[index][imageIndex]))
    # pictureLocation = pyautogui.locateOnScreen(images[index][imageIndex], confidence=0.9)
    # print(str(time.time()) + " " + str(pictureLocation))
    pictureLocations = pyautogui.locateAllOnScreen(images[index][imageIndex], confidence=0.9)
    # print(str(pictureLocations))
    pictureClicked = False
    locationList = []
    for pos in pictureLocations:
        if [pos[0], pos[1]] not in locationList:
            # locationList.append([pos[0], pos[1]])
            
            # locationList.append([pos[0]+1, pos[1]]) #@todo: figure out why it is picking up items 2nd time 1pxl in
            for x in range(-1, 3):
                locationList.append([pos[0], pos[1]+x])
                locationList.append([pos[0]+x, pos[1]+x])
                for y in range(-1, 3):
                    locationList.append([pos[0]+x, pos[1]+y]) 
            print(str(pos))
            pictureClicked = clickPicture(pos, images[index][imageIndex])
            sleepRandom(0.5, 2)
        
    print(str(locationList))        
    # list(pyautogui.locateAllOnScreen(images[index][imageIndex], confidence=0.9))
    # pictureClicked = clickPicture(pictureLocation, images[index][imageIndex])
    # print(str(pictureClicked))
    # if (pictureClicked == False):
    #     index += 1        
    #     clickPictures(images, index)
    if (pictureClicked == True):
        MouseAutomation.modifyLocationMove(current[0], current[1], 15)
    index += 1        
    clickPictures(images, index)
        

while (True == True):
    images = [
        ['bigBones.png'],
        ['smallBones.png'],
        ['beerGlass.png']
    ]
    # print(str(len(images)))
    clickPictures(images, 0)
    print("\n\n")
    sleepRandom(20, 60)
    