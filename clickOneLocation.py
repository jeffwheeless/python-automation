import pyautogui
import random
import time


def performLeftClickSleep(loc1):
    pyautogui.leftClick(
        random.randint(loc1[0]-10, loc1[0]+10),
        random.randint(loc1[1]-10, loc1[1]+10),
        0,
        random.uniform(0.3, 0.7)
    )
    sleepRandom(0.5, 0.9)


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    print(sleep)
    time.sleep(sleep)


foo = input("Mouse over first position ")
loc1 = pyautogui.position()
print(loc1)
foo = input("Mouse over first position ")

for x in range(1, 120):
    print(x)
    pyautogui.moveTo(
        random.randint(loc1[0]-10, loc1[0]+10),
        random.randint(loc1[1]-10, loc1[1]+10),
        random.uniform(0.3, 0.7)
    )
    sleepRandom(0.9, 1.4)
    performLeftClickSleep(loc1)
    performLeftClickSleep(loc1)
    sleepRandom(30.6, 50.5)
