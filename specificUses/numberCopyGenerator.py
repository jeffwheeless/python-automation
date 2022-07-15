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
    # global totalTime
    sleep = random.uniform(smallInt, largeInt)
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    time.sleep(sleep)
    # print(sleep)
    # time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))


print("\n\nGenerate random num, copy num, click and paste in box")
print("press tab, then type na in the comment box. You approve it.")
print(" [] <- put mouse there")
foo = input("Mouse over number generator location ")
loc1 = pyautogui.position()
foo = input("Mouse over hours box")
loc2 = pyautogui.position()

while (True == True):
    # current = pyautogui.position()
    pyautogui.moveTo(
        loc1[0],
        loc1[1],
        random.uniform(0.05, 0.2)
    )
    print(str(random.randint(6, 7)) + ":" + str(random.randint(10, 55)))
    performLeftClick(loc1)
    sleepRandom(0.03, 0.06)
    performLeftClick(loc1)
    sleepRandom(0.3, 0.5)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.keyDown('shift')
    sleepRandom(0.03, 0.06)
    pyautogui.press('c')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('shift')
    sleepRandom(0.3, 0.5)
    pyautogui.moveTo(
        loc2[0],
        loc2[1],
        random.uniform(0.05, 0.2)
    )
    sleepRandom(0.3, 0.5)
    performLeftClick(loc2)
    sleepRandom(0.3, 0.5)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.press('a')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.press('v')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.press('tab')
    sleepRandom(0.03, 0.06)
    pyautogui.write('na')
    foo = input("Next?")
