import pyautogui
import random
import time


def performLeftClick(loc1):
    pyautogui.leftClick(
        None,
        None,
        0,
        random.uniform(0.3, 0.7)
    )


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    print(sleep)
    time.sleep(sleep)


foo = input("Mouse over first position ")
loc1 = pyautogui.position()
print(loc1)
# foo = input("Mouse over first position ")

for x in range(1, 120):
    print(x)
    current = pyautogui.position()
    if (
        (current[0] >= loc1[0]+12 or current[0] <= loc1[0]-12) and
        (current[1] >= loc1[1]+12 or current[1] <= loc1[1]-12)
    ):
        pyautogui.moveTo(
            random.randint(loc1[0]-10, loc1[0]+10),
            random.randint(loc1[1]-10, loc1[1]+10),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(0.9, 1.4)
    performLeftClick(loc1)
    sleepRandom(0.3, 0.7)
    performLeftClick(loc1)
    sleepRandom(30.6, 52.5)
