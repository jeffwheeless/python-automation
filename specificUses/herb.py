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


foo = input("Mouse over banker position ")
loc1 = pyautogui.position()
# loc1 = [3323, 1086]
# loc1 = [2800, 700]
# loc1 = [500, 0]
print(loc1)
foo = input("Mouse over deposit all position ")
loc2 = pyautogui.position()
# loc2 = [2916, 1369]
# loc2 = [2800, 1200]
# loc2 = [500, 500]
print(loc2)
foo = input("Mouse over herb position ")
loc3 = pyautogui.position()
# loc3 = [2618, 924]
# loc3 = [3200, 1200]
# loc3 = [0, 500]
print(loc3)
foo = input("Mouse over herb in inv position ")
loc4 = pyautogui.position()
# loc4 = [3274, 1265]
# loc4 = [3200, 700]
# loc4 = [0, 0]
print(loc4)
# foo = input("Mouse over other window")
# loc5 = pyautogui.position()
# # loc5 = [1345, 998]
# print(loc5)


while (True == True):

    # runs = 10
    runs = input("How many runs: ")
    if (runs == ""):
        runs = 1
    runs = int(runs)
    print("Running for this many herbs: " + str(runs*28))
    # pyautogui.moveTo(
    #     loc1[0],
    #     loc1[1],
    #     random.uniform(0.1, 0.2),
    #     pyautogui.easeInBounce
    # )

    for x in range(0, runs):
        modloc1 = [
            random.randint(loc1[0]-2, loc1[0]+4),
            random.randint(loc1[1]-2, loc1[1]+4),
        ]
        modloc2 = [
            random.randint(loc2[0]-2, loc2[0]+2),
            random.randint(loc2[1]-2, loc2[1]+2),
        ]
        modloc3 = [
            random.randint(loc3[0]-2, loc3[0]+2),
            random.randint(loc3[1]-2, loc3[1]+2),
        ]
        modloc4 = [
            random.randint(loc4[0]-2, loc4[0]+2),
            random.randint(loc4[1]-2, loc4[1]+2),
        ]

        modloc1 = [
            random.randint(modloc1[0]-10, modloc1[0]+10),
            random.randint(modloc1[1]-10, modloc1[1]+10)
        ]
        modloc2 = [
            random.randint(modloc2[0]-3, modloc2[0]+3),
            random.randint(modloc2[1]-3, modloc2[1]+3)
        ]
        modloc3 = [
            random.randint(modloc3[0]-3, modloc3[0]+3),
            random.randint(modloc3[1]-3, modloc3[1]+3)
        ]
        modloc4 = [
            random.randint(modloc4[0]-3, modloc4[0]+3),
            random.randint(modloc4[1]-3, modloc4[1]+3)
        ]

        print("\nloop number:" + str(x))
        current = pyautogui.position()
        sleepRandom(1, 2)

        mouseMove(current[0], current[1], loc1[0], loc1[1])
        sleepRandom(0.4, 1)
        performLeftClick(pyautogui.position())
        sleepRandom(0.4, 1)
        if(random.randint(1, 2) == 1):
            performLeftClick(pyautogui.position())
            sleepRandom(0.4, 1)

        mouseMove(loc1[0], loc1[1], loc2[0], loc2[1])
        sleepRandom(0.4, 1)
        performLeftClick(pyautogui.position())
        sleepRandom(0.4, 1)

        mouseMove(loc2[0], loc2[1], loc3[0], loc3[1])
        sleepRandom(0.4, 1)
        performLeftClick(pyautogui.position())
        sleepRandom(0.4, 1)

        pyautogui.press('esc')
        sleepRandom(1.5, 2)

        mouseMove(loc3[0], loc3[1], loc4[0], loc4[1])
        sleepRandom(0.4, 1)
        performLeftClick(pyautogui.position())
        sleepRandom(0.4, 1)

        numHerbsDetermine = 3  # random.randint(2, 3)
        numHerbColumns = False
        numHerbRow = 3
        if(numHerbsDetermine == 2):
            numHerbRow = 7
        if(numHerbsDetermine == 3):
            numHerbRow = 7
            numHerbColumns = random.randint(5, 6)
            # print(numHerbColumns)
        went = False
        for x in range(1, numHerbRow):
            # sleepRandom(0.4, 1.2)
            if (numHerbColumns != False and x > (numHerbColumns-2)):
                if (went != True):
                    for y in range(0, 4):
                        moveWaitClick(
                            random.randint(
                                modloc4[0] - 5 + (50*y),
                                modloc4[0] + 5 + (50*y)
                            ),
                            random.randint(
                                modloc4[1] - 10 + (45*x),
                                modloc4[1] + 10 + (45*x)
                            ),
                        )
                        sleepRandom(0.3, 0.4)
                        # print("y: " + str(y))
                        # sleepRandom(1.9, 2.5)
                    went = True
                elif (went == True):
                    for y in range(3, -1, -1):
                        moveWaitClick(
                            random.randint(
                                modloc4[0] - 5 + (50*y),
                                modloc4[0] + 5 + (50*y)
                            ),
                            random.randint(
                                modloc4[1] - 10 + (45*x),
                                modloc4[1] + 10 + (45*x)
                            ),
                        )
                        sleepRandom(0.3, 0.4)
                    went = False
                # else:
                #     current = pyautogui.position()
                #     performLeftClick(current)
            else:
                moveWaitClick(
                    random.randint(
                        modloc4[0] - 10,
                        modloc4[0] + 10
                    ),
                    random.randint(
                        modloc4[1] - 10 + (45*x),
                        modloc4[1] + 10 + (45*x)
                    ),
                )
            sleepRandom(0.3, 0.4)
            # performLeftClick(pyautogui.position())
        # sleepRandom(0.4, 1)
        # current = pyautogui.position()
        # mouseMove(
        #     current[0], current[1],
        #     random.randint(100, 6000), random.randint(100, 1000)
        # )
        # sleepRandom(0.4, 1)
        # pyautogui.keyDown('alt')
        # sleepRandom(0.1, 0.2)
        # pyautogui.press('tab')
        # sleepRandom(0.1, 0.2)
        # pyautogui.keyUp('alt')
        # sleepRandom(20, 30)
        # sleepRandom(0.4, 1)
        # loc1 = [random.randint(loc1[0]-5, loc1[0]+5),
        #         random.randint(loc1[1]-5, loc1[1]+5)]
        # sleepRandom(0.4, 1)
        sleepRandom(6, 9)

    # print("\n\n----------------------")
    # current = pyautogui.position()
    # mouseMove(
    #     current[0],
    #     current[1],
    #     random.randint(loc5[0]-50, loc5[0]+50),
    #     random.randint(loc5[1]-50, loc5[1]+50)
    # )
    # foo = input("Mouse over herb position ")
    # loc3 = pyautogui.position()
    # print(loc3)
