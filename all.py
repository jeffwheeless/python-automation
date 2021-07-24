import pyautogui
import random
import numpy as np
import time
from scipy import interpolate
import math


def performLeftClick(loc):
    pyautogui.leftClick(
        None,
        None,
        # 0,
        # random.uniform(0.3, 0.7)
    )


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    print(sleep)
    # time.sleep(sleep)


def shuffleRandomize(loc, type, max):
    foo = 0
    min = 3
    if (max < min):
        foo = max
        max = min
        min = max
    if (type == 'add'):
        # print("("+str(loc)+"+"+str(time.time())[-1:], end="")
        # print(")+"+str(random.randint(3, max)), end="")
        # foo = (loc+int(str(time.time())[-1:]))+(random.randint(min, max)*1)
        foo = (loc+int(str(time.time())[-1:]))+random.randint(min, max)
        # print("=" + str(foo))
    else:
        # print("("+str(loc)+"-"+str(time.time())[-1:], end="")
        # print(")-"+str(random.randint(3, max)), end="")
        # foo = (loc-int(str(time.time())[-1:]))-(random.randint(min, max)*1)
        foo = (loc-int(str(time.time())[-1:]))-random.randint(min, max)
        # print("=" + str(foo))

    return foo


def clickRandom(loc, max, clickSpeed, offset1, offset2):
    # randLoc = 0  # random.randint(0, 2)
    current = pyautogui.position()
    xA = shuffleRandomize(loc[0]+offset1, 'sub', max)
    xB = shuffleRandomize(loc[0]+offset1, 'add', max)
    yA = shuffleRandomize(loc[1]+offset2, 'sub', max)
    yB = shuffleRandomize(loc[1]+offset2, 'add', max)
    mouseMoveSmooth(
        current[0],
        random.randint(xA, xB),
        current[1],
        random.randint(yA, yB),
    )
    pyautogui.click(
        random.randint(xA, xB),
        random.randint(yA, yB),
        _pause=False,
        duration=clickSpeed
    )


def drawArea(loc):
    max = 10
    pyautogui.press('x')
    # pyautogui.press('[')
    # pyautogui.press('[')
    for x in range(0, max, 25):
        pyautogui.click(loc[0]+(max*1), loc[1]+(max*1))
        pyautogui.dragTo(loc[0]-(max*1), loc[1]+(max*1))
        pyautogui.dragTo(loc[0]-(max*1), loc[1]-(max*1))
        pyautogui.dragTo(loc[0]+(max*1), loc[1]-(max*1))
        pyautogui.dragTo(loc[0]+(max*1), loc[1]+(max*1))
        # pyautogui.dragTo(loc[randLoc][0]-x, loc[randLoc][1]+x)
        # pyautogui.dragTo(loc[randLoc][0]+x, loc[randLoc][1]+x, button='left')
        # pyautogui.dragTo(loc[randLoc][0]+x, loc[randLoc][1]-x, button='left')
        # pyautogui.dragTo(loc[randLoc][0]-x, loc[randLoc][1]-x, button='left')
    pyautogui.press('x')
    # pyautogui.press(']')
    # pyautogui.press(']')


def point_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def getDiff(locA, locB):
    diff = locA - locB
    if(locA < locB):
        diff = locB - locA

    return diff


def mouseMoveSmooth(x1, x2, y1, y2):
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
    tck, u = interpolate.splprep([x, y], k=degree)
    # Move upto a certain number of points
    numMade = random.randint(1, 4)
    u = np.linspace(0, 1, num=numMade + int(point_dist(x1, y1, x2, y2)/50.0))
    points = interpolate.splev(u, tck)

    # Move mouse.
    duration = 0.1
    timeout = duration / len(points[0])
    point_list = zip(*(i.astype(int) for i in points))
    for point in point_list:
        pyautogui.moveTo(*point, _pause=False)
        time.sleep(timeout)
        currentLoc = pyautogui.position()
        pyautogui.press('x')
        pyautogui.click(currentLoc, duration=clickSpeed, _pause=False)
        pyautogui.press('x')


max = 8  # input("Max pixels to go out to ")
go = "y"
clickSpeed = 0.125
total = 0
offsetLoc = [2, 4, 1]
cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
loc = []
foo = input("Mouse over start position ")
loc.append(pyautogui.position())
foo = input("Mouse over end position ")
loc.append(pyautogui.position())
pyautogui.click(loc[0][0], loc[0][1], _pause=False)
pyautogui.press('delete')

print(loc)


for index in range(0, len(loc)-1, 2):
    pyautogui.click(loc[index][0], loc[index+1][1], _pause=False)
    # drawArea(loc[index])
    # drawArea(loc[index+1])
    for temp in range(0, 25):

        diffX = 0
        xIncrement = 0
        diffY = 0
        yIncrement = 0
        # # loc[index][0] = loc[index][0] + (temp * 10)
        # loc[index][1] = loc[index][1] + (temp * 10)
        # # loc[index+1][0] = loc[index+1][0] + (temp * 10)
        # loc[index+1][1] = loc[index+1][1] + (temp * 10)
        sections = random.randint(2, 5)

        randNumber = random.randint(2, 4)
        pyautogui.moveTo(loc[index][0], loc[index][1], _pause=False)
        # if(randNumber == 1):
        #     clickRandom(loc[index], max, clickSpeed, 0, 0)
        if(randNumber == 2):
            clickRandom(loc[index], max, clickSpeed, -
                        offsetLoc[0], -offsetLoc[1])
        elif(randNumber == 3):
            clickRandom(loc[index], max, clickSpeed,
                        offsetLoc[1], offsetLoc[2])
        elif(randNumber == 4):
            clickRandom(loc[index], max, clickSpeed,
                        offsetLoc[2], offsetLoc[0])

        currentLoc = pyautogui.position()
        pyautogui.click(currentLoc, duration=clickSpeed, _pause=False)
        # loc[index] = pyautogui.position()
        # pyautogui.click(loc[index][0], loc[index][1], _pause=False)
        diffX = getDiff(loc[index][0], loc[index+1][0])
        xIncrement = round(diffX/sections)
        diffY = getDiff(loc[index][1], loc[index+1][1])
        yIncrement = round(diffY/sections)
        baseMove = 2

        if (abs(diffX) < 75 or abs(diffY) < 75):
            mouseMoveSmooth(
                loc[index][0],
                loc[index+1][0]+random.randint(-5, 5),
                loc[index][1],
                loc[index+1][1]+random.randint(-5, 5),
            )
            continue

        for i in range(0, sections):
            currentLoc = pyautogui.position()
            diffX = getDiff(currentLoc[0], loc[index+1][0])
            xIncrement = round(diffX/(sections-i))
            diffY = getDiff(currentLoc[1], loc[index+1][1])
            yIncrement = round(diffY/(sections-i))
            mouseMoveSmooth(
                currentLoc[0],
                currentLoc[0]+xIncrement+random.randint(-baseMove, baseMove),
                currentLoc[1],
                currentLoc[1]+yIncrement+random.randint(-baseMove, baseMove)
            )
            pyautogui.press('x')
            currentLoc = pyautogui.position()
            pyautogui.click(currentLoc, duration=clickSpeed, _pause=False)

        if(random.randint(1, 10) > 8):
            currentLoc = pyautogui.position()
            mouseMoveSmooth(
                currentLoc[0],
                currentLoc[0]+random.randint(-baseMove, baseMove),
                currentLoc[1],
                currentLoc[1]+random.randint(-baseMove, baseMove)
            )

        randNumber = random.randint(2, 4)
        # pyautogui.moveTo(loc[index+1][0], loc[index+1][1], _pause=False)
        # if(randNumber == 1):
        #     clickRandom(loc[index], max, clickSpeed, 0, 0)
        if(randNumber == 2):
            clickRandom(loc[index+1], max, clickSpeed, -
                        offsetLoc[0], -offsetLoc[1])
        elif(randNumber == 3):
            clickRandom(loc[index+1], max, clickSpeed,
                        offsetLoc[1], offsetLoc[2])
        elif(randNumber == 4):
            clickRandom(loc[index+1], max, clickSpeed,
                        offsetLoc[2], offsetLoc[0])
        currentLoc = pyautogui.position()
        mouseMoveSmooth(
            currentLoc[0],
            loc[index+1][0]+random.randint(-5, 5),
            currentLoc[1],
            loc[index+1][1]+random.randint(-5, 5),
        )
        # pyautogui.dragTo(loc[index][0], loc[index+1][1], _pause=False)
        currentLoc = pyautogui.position()
        pyautogui.click(currentLoc, duration=clickSpeed, _pause=False)
    # pyautogui.press('[')
    # pyautogui.dragTo(loc[0][0], loc[index][1], _pause=False)
