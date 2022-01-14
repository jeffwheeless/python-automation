
import time
import pyautogui
import random
import os

def writeSleepEnter(typedString):
    pyautogui.write(typedString)
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('enter')


def sleepRandom(smallInt, largeInt):
    sleep = round(random.uniform(smallInt, largeInt), 10)
    print(formatHumanTimeString(sleep))
    time.sleep(sleep)


def formatHumanTimeString(seconds):
    timeLeftMin = round((seconds) // 60)
    timeLeftSec = ("0" if ((seconds) % 60) <
                   10 else "") + str(round(seconds % 60, 5))
    return str(timeLeftMin) + ":" + str(timeLeftSec)


wordCount = input("Hover over text box location ")
mainLocation = pyautogui.position()
wordCount = input("Hover over sell button location ")
sellbutton = pyautogui.position()

itemsToSell = ["+sell 55 Bronze bolts", "+sell 14 Bronze arrow", "+sell 273 Bronze platebody", "+sell 5 Bronze spear", "+sell 1 Bronze axe", "+sell 4 Bronze bar", "+sell 10 Dwarven stout", "+sell 2 Cabbage", "+sell 1 Iron full helm", "+sell 167 Iron platebody", "+sell 3 Iron sword", "+sell 8 Purple firelighter", "+sell 2 Black bead", "+sell 3 Red bead", "+sell 6 White bead", "+sell 5 Yellow bead"]

for i in range(0, len(itemsToSell)):
    pyautogui.leftClick(mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
    writeSleepEnter(itemsToSell[i])
    print("Item: " + itemsToSell[i])
    sleepRandom(2, 3)
    pyautogui.leftClick(sellbutton[0], sellbutton[1], 0, random.uniform(0.3, 0.7))
    sleepRandom(2, 4)
print("done")
quit()