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


def mouseAction(row, column):
    diffRange = 15
    x = ((28 * column) + (22 * column)) + loc1[0]
    y = (43 * row) + loc1[1]
    pyautogui.moveTo(x-diffRange, y-diffRange)
    pyautogui.dragTo(x-diffRange, y+diffRange, button='left')
    pyautogui.dragTo(x+diffRange, y+diffRange, button='left')
    pyautogui.dragTo(x+diffRange, y-diffRange, button='left')
    pyautogui.dragTo(x-diffRange, y-diffRange, button='left')
    # sleepRandom(0.9, 1.4)
    # performLeftClickSleep(loc1)
    # performLeftClickSleep(loc1)
    # sleepRandom(30.6, 50.5)


def mouseActionRow(row):
    if ((row % 2) == 0):
        for column in range(3, -1, -1):
            mouseAction(row, column)
    else:
        for column in range(0, 4):
            mouseAction(row, column)


def mouseActionColumn(column):
    if ((column % 2) == 0):
        for row in range(5, 0, -1):
            mouseAction(row, column)
    else:
        for row in range(1, 5):
            mouseAction(row, column)


    # foo = input("Mouse over first position ")
    # loc1 = pyautogui.position()
loc1 = [3407, 1300]
print(loc1)
# foo = input("Mouse over first position ")
pyautogui.moveTo(
    random.randint(loc1[0]-10, loc1[0]+10),
    random.randint(loc1[1]-10, loc1[1]+10),
    random.uniform(0.3, 0.7)
)
pyautogui.click()
pyautogui.press('delete')
pyautogui.keyDown('shift')

rand = random.randint(1, 4)
# if (rand == 1):
#     for row in range(0, 6):
#         mouseActionRow(row)
# if (rand == 2):
for column in range(0, 4):
    mouseActionColumn(column)
# if (rand == 3):
# for row in range(5, -1, -1):
#     mouseActionRow(row)
# if (rand == 4):
#     for column in range(4, 0, -1):
#         for row in range(6, 0, -1):
#             mouseAction(row, column)
# for row in range(0, 6):
#     for column in range(0, 4):
#         mouseAction(row, column)
pyautogui.keyUp('shift')
