import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

cp = random.randint(3, 5)  # Number of control points. Must be at least 2.


def performLeftClick(loc1):
    # print("Clicking")
    pyautogui.leftClick(
        loc1[0],  # None,
        loc1[1],  # ,  # None,
        # 0,
        random.uniform(0.01, 0.02)
    )


def performRightClick(loc1):
    pyautogui.rightClick(
        loc1[0],  # None,
        loc1[1]  # ,  # None,
        # 0,
        # random.uniform(0.3, 0.7)
    )


def point_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def sleepRandom(smallInt, largeInt):
    # global totalTime
    sleep = random.uniform(smallInt, largeInt)
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    time.sleep(sleep)
    print(sleep)
    # time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))


def mouseMoveSmooth(x1, x2, y1, y2):
    global cp
    # Distribute control points between start and destination evenly.
    x = np.linspace(x1, x2, num=cp, dtype='int')
    y = np.linspace(y1, y2, num=cp, dtype='int')

    # Randomise inner points a bit (+-RND at most).
    # RND = 10
    RND = []
    for i in range(0, 4):
        RND.append(random.randint(2, 10))
    xr = [random.randint(-RND[0], RND[1]) for k in range(cp)]
    yr = [random.randint(-RND[2], RND[3]) for k in range(cp)]
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline.
    degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
    # Must be less than number of control points.
    # print("cp: " + str(cp) + " || degree: " + str(degree))
    tck, u = interpolate.splprep(
        [x, y],
        k=degree
    )
    # Move upto a certain number of points
    numMade = 10  # random.randint(3, 15)
    u = np.linspace(0, 1, num=numMade + int(point_dist(x1, y1, x2, y2)/50.0))
    points = interpolate.splev(u, tck)

    # Move mouse.
    duration = 0.1
    timeout = duration / len(points[0])
    point_list = zip(*(i.astype(int) for i in points))
    for point in point_list:
        # current = pyautogui.position()
        # performLeftClick(current)
        # pyautogui.leftClick(*point)
        pyautogui.moveTo(
            *point,
            _pause=False  # ,
            # duration=random.uniform(0.03, 0.09)
        )
        # pyautogui.dragTo(*point, _pause=False)
        time.sleep(timeout)


def mouseMove(x1, y1, x2, y2):
    smallerX = x1
    xDiff = x2-x1
    smallerY = y1
    yDiff = y2-y1
    if (x1 > x2):
        smallerX = x2
    if (xDiff <= 0):
        xDiff = 5
    if (y1 > y2):
        smallerY = y2
        yDiff = y1-y2+4
    if (yDiff <= 0):
        yDiff = 5

    xDiffRatio = 75
    if (xDiff > 200):
        xDiffRatio = round(xDiff*.5)+4
    xHalf = round(xDiff*random.uniform(0.05, 0.95)) + \
        smallerX + random.randint((xDiffRatio*-1), xDiffRatio)
    xHalfAlt = round(xDiff*random.uniform(0.05, 0.95)) + \
        smallerX + random.randint((xDiffRatio*-1), xDiffRatio)

    yDiffRatio = 75
    if (yDiff > 200):
        yDiffRatio = round(yDiff*.5)+4
    yHalf = round(yDiff*random.uniform(0.05, 0.95)) + \
        smallerY + random.randint((yDiffRatio*-1), yDiffRatio)
    yHalfAlt = round(yDiff*random.uniform(0.05, 0.95)) + \
        smallerY + random.randint((yDiffRatio*-1), yDiffRatio)

    # performLeftClick([xHalf, yHalf])
    # performLeftClick([xHalfAlt, yHalfAlt])
    # print("1s: " + str(x1) + ", " + str(y1))
    # print("first halfs: " + str(xHalf) + ", " + str(yHalf))
    # print("2nd halfs: " + str(xHalfAlt) + ", " + str(yHalfAlt))
    # print("2s: " + str(x2) + ", " + str(y2))
    # print("++++++++++++++\nDiff X:" + str(xDiff))
    # print("Diff Y:" + str(yDiff))

    x1New = x1 + random.randint(-15, 15)
    xHalfNew = xHalf + random.randint(-15, 15)
    xHalfAltNew = xHalfAlt + random.randint(-15, 15)
    x2New = x2 + random.randint(-15, 15)
    y1New = y1 + random.randint(-15, 15)
    yHalfNew = yHalf + random.randint(-15, 15)
    yHalfAltNew = yHalfAlt + random.randint(-15, 15)
    y2New = y2 + random.randint(-15, 15)

    decider = random.randint(1, 10)
    if (decider <= 3):
        foo = True  # print("holder")
    elif (decider >= 8):
        xHalfNew = xHalfAltNew
        yHalfNew = yHalfAltNew
    else:
        xHalf = [xHalfAltNew, xHalfNew]
        if (xHalf[0] > xHalf[1]):
            xHalf = [xHalfNew, xHalfAltNew]
        yHalf = [yHalfAltNew, yHalfNew]
        if (yHalf[0] > yHalf[1]):
            yHalf = [yHalfNew, yHalfAltNew]
        xHalfNew = random.randint(xHalf[0], xHalf[1])
        yHalfNew = random.randint(yHalf[0], yHalf[1])

    mouseMoveSmooth(x1New, xHalfNew, y1New, yHalfNew)
    if (random.randint(1, 10) >= 8):
        # current = pyautogui.position()
        # performLeftClick(current)
        mouseMoveSmooth(xHalfNew, x2, yHalfNew, y2)
        xHalf = [x2, x2New]
        if (xHalf[0] > xHalf[1]):
            xHalf = [x2New, x2]
        yHalf = [y2, y2New]
        if (yHalf[0] > yHalf[1]):
            yHalf = [y2New, y2]
        xHalfNew = random.randint(xHalf[0], xHalf[1])
        yHalfNew = random.randint(yHalf[0], yHalf[1])
        mouseMoveSmooth(x2, x2New, y2, y2New)
    else:
        mouseMoveSmooth(xHalfNew, x2New, yHalfNew, y2New)
    # pyautogui.moveTo(x2, y2)
    # current = pyautogui.position()
    # pyautogui.press('x')
    sleepRandom(0.4, 1)
    # performLeftClick(current)
    # pyautogui.press('x')
    sleepRandom(0.4, 1)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+4 or current[0] <= mainLoc[0]-4):
        foo = input("Move out of zone, get close and hit enter")
        pyautogui.moveTo(
            mainLoc[0] + random.randint(-3, 3),
            mainLoc[1] + random.randint(-3, 3),
            random.uniform(0.3, 0.7)
        )
        sleepRandom(
            random.uniform(0.4, 0.6),
            random.uniform(0.6, 0.8)
        )
        current = pyautogui.position()

    return current


def moveWaitClick(x, y, speed=0.1):
    # mouseOutOfRange([x, y])
    # print("Moving")
    pyautogui.moveTo(
        x,
        y,
        speed
    )
    sleepRandom(0.3, 0.6)
    mouseOutOfRange([x, y])
    performLeftClick(pyautogui.position())


# foo = input("Mouse over banker position ")
# loc1 = pyautogui.position()
# # loc1 = [3323, 1086]
# # loc1 = [2800, 700]
# # loc1 = [500, 0]
# print(loc1)
# locationRuns = input("How many run locations: ")
# locationRuns = int(locationRuns)
locationRuns = 13
loc = []
print("Apped to postion input to add key")
print("1) Esc  2) Space  3) Alt+tab")
for temp in range(0, locationRuns):
    with open('output.txt', 'a') as f:
        extraKey = input("Mouse over " + str(temp+1) + " position ")
        current = pyautogui.position()

        loc.append([current[0], current[1], '', 3, 3])
        # loc1 = pyautogui.position()
        # loc1 = [3323, 1086]
        # loc1 = [2800, 700]
        # loc1 = [500, 0]
        f.write(str(loc[temp]))

loc.append([2535, 796, '', 3, 6])  # first
loc.append([2777, 888, '', 3, 6])
loc.append([2576, 921, '', 3, 6])
loc.append([2721, 1095, '', 3, 6])
loc.append([2788, 1173, '', 3, 6])
loc.append([2778, 1307, '', 3, 6])
loc.append([2841, 1103, '', 3, 6])
loc.append([2841, 1103, '', 3, 6])
loc.append([2931, 1138, '', 3, 6])
loc.append([2931, 1138, '', 3, 6])
loc.append([3080, 1058, '', 3, 6])
loc.append([2807, 889, '', 3, 6])
loc.append([2788, 887, '', 3, 6])

foo = input("Mouse over banker position ")
mainLoc = pyautogui.position()
while (True == False):
    foo = input("Mouse over banker position ")
    # current = pyautogui.position()
    # mouseMove(current[0], current[1], mainLoc[0], mainLoc[0])
    # for x in range(0, 130):
    #     performLeftClick(pyautogui.position())
    #     sleepRandom(0.1, 0.5)

    # pyautogui.keyDown('alt')
    # sleepRandom(0.1, 0.2)
    # pyautogui.press('tab')
    # sleepRandom(0.1, 0.2)
    # pyautogui.keyUp('alt')
    # foo = input("Mouse over banker position ")
    # pyautogui.keyDown('alt')
    # sleepRandom(0.1, 0.2)
    # pyautogui.press('tab')
    # sleepRandom(0.1, 0.2)
    # pyautogui.keyUp('alt')
    # sleepRandom(0.05, 0.1)
    # current = pyautogui.position()
    # mouseMove(current[0], current[1], loc[0][0], loc[0][1])
    # pyautogui.keyDown('shift')
    # for temp in range(0, locationRuns):
    #     modloc = [
    #         random.randint(loc[temp][0]-loc[temp][3],
    #                        loc[temp][0]+loc[temp][3]),
    #         random.randint(loc[temp][1]-loc[temp][3],
    #                        loc[temp][1]+loc[temp][3]),
    #     ]

    #     current = pyautogui.position()

    #     pyautogui.moveTo(
    #         loc[temp][0],
    #         loc[temp][1],
    #         duration=random.uniform(0.1, 0.2)
    #     )
    #     # mouseMove(current[0], current[1], loc[temp][0], loc[temp][1])
    #     sleepRandom(0.01, 0.05)
    #     performLeftClick(pyautogui.position())
    #     sleepRandom(0.05, 0.1)

# Go to furnace
    current = pyautogui.position()
    mouseMove(current[0], current[1], loc[0][0], loc[0][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(10, 12)
    current = pyautogui.position()
    mouseMove(current[0], current[1], loc[1][0], loc[1][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(5, 10)
    current = pyautogui.position()
# walk to trader
    mouseMove(current[0], current[1], loc[2][0], loc[2][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    mouseMove(current[0], current[1], loc[3][0], loc[3][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    mouseMove(current[0], current[1], loc[4][0], loc[4][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    mouseMove(current[0], current[1], loc[5][0], loc[5][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    sleepRandom(10, 12)
    foo = input("Mouse over banker position ")

    pyautogui.keyDown('shift')
    mouseMove(current[0], current[1], loc[6][0], loc[6][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    mouseMove(current[0], current[1], loc[7][0], loc[7][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    mouseMove(current[0], current[1], loc[8][0], loc[8][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)
    mouseMove(current[0], current[1], loc[9][0], loc[9][1])
    sleepRandom(0.01, 0.05)
    performLeftClick(pyautogui.position())
    sleepRandom(1, 2)

    # pyautogui.keyDown('ctrl')
    # pyautogui.press('d')
    # pyautogui.keyUp('ctrl')

    pyautogui.keyUp('shift')
    # pyautogui.keyUp('shift')

    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
    # sleepRandom(3, 5)
