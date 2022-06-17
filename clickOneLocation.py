import pyautogui
import random
import time


def performLeftClick(loc1):
    pyautogui.leftClick(
        loc1[0],  # None,
        loc1[1]  # ,  # None,
        # 0,
        #random.uniform(0.3, 0.7)
    )


def performRightClick(loc1):
    pyautogui.rightClick(
        loc1[0],  # None,
        loc1[1]  # ,  # None,
        # 0,
        #random.uniform(0.3, 0.7)
    )


def sleepRandom(smallInt, largeInt):
    #sleep = random.uniform(smallInt, largeInt)
    # print(sleep)
    # time.sleep(sleep)
    time.sleep(random.uniform(smallInt, largeInt))


foo = input("Mouse over first position ")
loc1 = pyautogui.position()
print(loc1)
# foo = input("Mouse over first position ")

while (True == True):
    #maxRange = random.randint(100, 250)
    for x in range(1, 250):
        # print(x)
        current = pyautogui.position()
        if (
            x % 2 == 0 and
           (current[0] >= loc1[0]+12 or current[0] <= loc1[0]-12) and
           (current[1] >= loc1[1]+12 or current[1] <= loc1[1]-12)
           ):
            foo = input("Mouse over first position ")
            loc1 = pyautogui.position()
            # pyautogui.moveTo(
            #     random.randint(loc1[0]-10, loc1[0]+10),
            #     random.randint(loc1[1]-10, loc1[1]+10),
            #     random.uniform(0.3, 0.7)
            # )
            # sleepRandom(0.9, 1.4)
        # performRightClick(loc1)
        # sleepRandom(0.03, 0.2)
        performLeftClick(loc1)
        sleepRandom(0.3, 0.5)
        # sleepRandom(2.6, 4)
        # pyautogui.write('1')
        # sleepRandom(0.03, 0.05)
        # sleepRandom(1, 2)
        # performLeftClick(loc1)
        #sleepRandom(30.6, 4*60)
    foo = input("Mouse over first position ")
