import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
total = 0
totalTimeStamped = 0
averageTimeStamped = 22.760091972351074


def performLeftClick(xy):
    pyautogui.leftClick(
        xy[0],  # None,
        xy[1]  # ,  # None,
        # 0,
        # random.uniform(0.3, 0.7)
    )


def performRightClick(xy):
    pyautogui.rightClick(
        xy[0],  # None,
        xy[1]  # ,  # None,
        # 0,
        # random.uniform(0.3, 0.7)
    )


def point_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def sleepRandom(smallInt, largeInt):
    # global totalTime
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    # print(sleep)
    time.sleep(sleep)
    # time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))

    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 1)

    if (random.randint(1, 1000) > 925):
        sleepRandom(1, 2)

    if (random.randint(1, 1000) > 960):
        sleepRandom(1, 3)

    if (random.randint(1, 1000) > 995):
        sleepRandom(1, 20)


def mouseMoveSmooth(x1, x2, y1, y2):
    # pyautogui.moveTo(
    #     x2,
    #     y2
    # )
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
            _pause=False,
            duration=random.uniform(0.03, 0.09)
        )
        # pyautogui.dragTo(*point, _pause=False)
        duration = random.uniform(0.1, 0.3)
        timeout = duration / len(points[0])
        time.sleep(timeout)


def mouseMove(x1, y1, x2, y2):
    if (
        x1 <= x2+20 and x1 >= x2-20 and
        y1 <= y2+20 and y1 >= y2-20
    ):
        print("Super Small distance detected, not moving")
        # pyautogui.moveTo(x2, y2, 0.17)
    elif (
        x1 <= x2+40 and x1 >= x2-40 and
        y1 <= y2+40 and y1 >= y2-40
    ):
        print("Small distance detected, moving quicker")
        pyautogui.moveTo(x2, y2, 0.17)
    else:
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
            melarky = True
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

        # time.sleep(random.uniform(0.0001, 0.1))
        # time.sleep(random.uniform(0.5, 1))
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
        # sleepRandom(0.7, 1.2) #sleepRandom(1, 1.5)
        # performLeftClick(current)
        # pyautogui.press('x')
        # sleepRandom(0.7, 1.2) #sleepRandom(1, 1.5)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+20 or current[0] <= mainLoc[0]-20):
        print(str(mainLoc) + " is not close to current loc of " + str(current))
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


# locationRuns = input("How many run locations: ")
# locationRuns = int(locationRuns)
locationRuns = 5
loc = []
# print("Apped to postion input to add key")
# print("1) Esc  2) Space  3) Alt+tab")
# for temp in range(0, locationRuns-1):

#     with open('output.txt', 'a') as f:
#         extraKey = input("Mouse over " + str(temp+1) + " position ")
#         current = pyautogui.position()
#         if (extraKey != "" and int(extraKey) >= 0):
#             extraKey = int(extraKey)

#         distVariation = input("Distance variation between clicks ")
#         if (distVariation == ""):
#             distVariation = "5"
#         elif (int(distVariation) > 4):
#             distVariation = "4"

#         timeVariation = input("Time between clicks ")
#         if (timeVariation == ""):
#             timeVariation = "10"

#         loc.append([current[0], current[1], extraKey,
#                     int(distVariation), int(timeVariation)])
#         # loc1 = pyautogui.position()
#         # loc1 = [3323, 1086]
#         # loc1 = [2800, 700]
#         # loc1 = [500, 0]
#         print(loc[temp])
#         f.write("loc.append(" + str(loc[temp]) + ")")

loc.append([3420, 1327, '', 2, 1])
loc.append([2751, 792, '', 2, 1])
loc.append([2051, 1125, '', 2, 1])
loc.append([2215, 1555, '', 4, 7])
loc.append([3333, 969, '', 2, 80])

runs = 1
startAt = input("Starting location of the " + str(locationRuns) + ": ")
if (startAt == ""):
    startAt = 1
startAt = int(startAt)-1
while (True == True):

    runs = 1
    runs = int(input("How many runs: "))
    if (runs == "" or runs < 2):
        runs = 1
    else:
        runs = round(int(runs))

    print("Expected Run Time: " + str(averageTimeStamped*locationRuns*runs))
    # print("Running for this many herbs: " + str(runs*28))
    # pyautogui.moveTo(
    #     loc1[0],
    #     loc1[1],
    #     random.uniform(0.1, 0.2),
    #     pyautogui.easeInBounce
    # )

    for x in range(0, runs):
        # print("loop number:" + str(x) + " of " + str(runs))
        for temp in range(startAt, locationRuns):
            startTime = time.time()
            total = total + 1
            print("Item #" + str(temp+1) + " of " + str(locationRuns) +
                  " || " + str(loc[temp]) + " || loop number:" + str(x+1) + " of " + str(runs))
            # print(str(loc[temp]))
            # print("Sleep Time: " + str(loc[temp][4]))
            modloc = [
                random.randint(loc[temp][0]-loc[temp][3],
                               loc[temp][0]+loc[temp][3]),
                random.randint(loc[temp][1]-loc[temp][3],
                               loc[temp][1]+loc[temp][3]),
            ]

            if (random.randint(0, 1) == 0):
                current = pyautogui.position()
                if (
                    current[0] <= modloc[0]+5 and current[0] >= modloc[0]-5 and
                    current[1] <= modloc[1]+5 and current[1] >= modloc[1]-5
                ):
                    print("Next loc is very close, staying still")
                else:
                    mouseMove(current[0], current[1], modloc[0], modloc[1])
                sleepRandom(0.05, 0.1)
                sleepRandom(loc[temp][4]-0.5, loc[temp][4]+0.5)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())
            else:
                sleepRandom(loc[temp][4]-0.5, loc[temp][4]+0.5)
                current = pyautogui.position()
                if (
                    current[0] <= modloc[0]+5 and current[0] >= modloc[0]-5 and
                    current[1] <= modloc[1]+5 and current[1] >= modloc[1]-5
                ):
                    print("Next loc is very close, staying still")
                else:
                    mouseMove(current[0], current[1], modloc[0], modloc[1])
                sleepRandom(0.05, 0.1)
                mouseOutOfRange(modloc)
                performLeftClick(pyautogui.position())

            sleepRandom(0.5, 1)
            if (loc[temp][2] == '1'):
                pyautogui.press('esc')
            elif (loc[temp][2] == '2'):
                pyautogui.press('space')
            elif (loc[temp][2] == '3'):
                pyautogui.keyDown('alt')
                sleepRandom(0.1, 0.2)
                pyautogui.press('tab')
                sleepRandom(0.1, 0.2)
                pyautogui.keyUp('alt')
            sleepRandom(0.5, 1)

            runTimeStamped = (time.time()-startTime)
            totalTimeStamped = totalTimeStamped + runTimeStamped
            averageTimeStamped = totalTimeStamped/total
            print("Iteration took: " + str(runTimeStamped) + "s")

        sleepRandom(8, 10)
    print("Average Time Stamped took: " + str(averageTimeStamped) + "s")

    startAt = 0

    print("\n\n----------------------")
