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
        _pause=False
    )


def sleepRandom(smallInt, largeInt):
    # global altWindowXY
    sleep = round(random.uniform(smallInt, largeInt), 10)
    # print(sleep)

    # if (random.randint(1, 1000) > 995):
    #     sleepRandom(10, 20)
    # elif (random.randint(1, 1000) > 980):
    #     sleepRandom(2, 5)
    # elif (random.randint(1, 1000) > 900):
    #     sleepRandom(1, 3)
    if (random.randint(1, 1000) > 850):
        sleepRandom(0, 2)

    time.sleep(sleep)


def shuffleRandomize(loc, type, max):
    foo = 0
    min = 3
    if (max < min):
        foo = max
        max = min
        min = max
    if (type == 'add'):
        foo = (loc+int(str(time.time())[-1:]))+random.randint(min, max)
    else:
        foo = (loc-int(str(time.time())[-1:]))-random.randint(min, max)

    return foo


def clickRandom(loc, max, clickSpeed, offset1, offset2):
    current = pyautogui.position()
    xA = shuffleRandomize(current[0]+offset1, 'sub', max)
    xB = shuffleRandomize(current[0]+offset1, 'add', max)
    yA = shuffleRandomize(current[1]+offset2, 'sub', max)
    yB = shuffleRandomize(current[1]+offset2, 'add', max)
    randX = random.randint(xA, xB)
    randY = random.randint(yA, yB)
    try:
        mouseMoveSmooth(
            current[0],
            randX,
            current[1],
            randY,
            round(random.uniform(0.05, 0.1), 10)
        )
    except:
        print("randX: " + str(randX) + "\trandY: " + str(randY))


def drawArea(loc):
    max = 75
    pyautogui.press('x')
    # pyautogui.press('[')
    # pyautogui.press('[')
    for x in range(0, max, 25):
        pyautogui.click(loc[0]+(max*1), loc[1]+(max*1), _pause=False)
        pyautogui.dragTo(loc[0]-(max*1), loc[1]+(max*1), _pause=False)
        pyautogui.dragTo(loc[0]-(max*1), loc[1]-(max*1), _pause=False)
        pyautogui.dragTo(loc[0]+(max*1), loc[1]-(max*1), _pause=False)
        pyautogui.dragTo(loc[0]+(max*1), loc[1]+(max*1), _pause=False)
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
    # diff = locA - locB
    # if(locA < locB):
    diff = locB - locA

    return diff


def getTween():

    randNumber = random.randint(1, 4)
    if(randNumber == 1):
        return pyautogui.easeInQuad
    elif(randNumber == 2):
        return pyautogui.easeOutQuad
    elif(randNumber == 3):
        return pyautogui.easeInOutQuad
    elif(randNumber == 4):
        return pyautogui.easeInBounce


def mouseMoveSmooth(x1, x2, y1, y2, suggestedDuration):
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
    try:
        tck, u = interpolate.splprep([x, y], k=degree)
        # Move upto a certain number of points
        numMade = random.randint(1, 4)
        u = np.linspace(0, 1, num=numMade +
                        int(point_dist(x1, y1, x2, y2)/50.0))
        points = interpolate.splev(u, tck)

        # Move mouse.
        duration = 0.1
        timeout = duration / len(points[0])
        point_list = zip(*(i.astype(int) for i in points))

        for point in point_list:
            pyautogui.moveTo(
                *point,
                duration=suggestedDuration,
                tween=getTween(),
                _pause=False
            )
            currentLoc = pyautogui.position()
        print(".", end="")
    except:
        print("F", end="")


max = 8  # input("Max pixels to go out to ")
go = "y"
clickSpeed = 0.125
total = 0
offsetLoc = [1, 2, 4]
cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
loc = []
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())

loc.append([2576, 952])
loc.append([2632, 952])
loc.append([2632, 952])
loc.append([3417, 1475])
loc.append([3413, 1475])
loc.append([3463, 1469])
loc.append([3463, 1469])
loc.append([2834, 1453])
loc.append([2834, 1453])
loc.append([2577, 953])

pyautogui.moveTo(
    loc[0][0],
    loc[0][1],
    duration=round(random.uniform(0.05, 0.1), 10),
    tween=pyautogui.easeInQuad,
    _pause=False
)

print(loc)

for temp in range(0, 1):
    if (temp > 0):
        print("\t\t\t-- Run: " + str(temp))
    for index in range(0, len(loc)-1, 2):
        diffX = 0
        xIncrement = 0
        diffY = 0
        yIncrement = 0
        sections = random.randint(10, 30)
        # sections = random.randint(40, 60)

        randNumber = random.randint(1, 3)
        # pyautogui.moveTo(
        #     loc[index][0],
        #     loc[index][1],
        #     duration=round(random.uniform(0.3, 0.5), 10),
        #     tween=pyautogui.easeInQuad,
        #     _pause=False
        # )
        if(randNumber == 1):
            clickRandom(loc[index], max, clickSpeed,
                        offsetLoc[0], offsetLoc[1])
        elif(randNumber == 2):
            clickRandom(loc[index], max, clickSpeed,
                        offsetLoc[1], offsetLoc[2])
        elif(randNumber == 3):
            clickRandom(loc[index], max, clickSpeed,
                        offsetLoc[0], offsetLoc[2])

        currentLoc = pyautogui.position()
        diffX = getDiff(currentLoc[0], loc[index+1][0])
        xIncrement = round(diffX/sections)
        diffY = getDiff(currentLoc[1], loc[index+1][1])
        yIncrement = round(diffY/sections)
        baseMove = 2

        if (abs(diffX) < 75 and abs(diffY) < 75):
            currentLoc = pyautogui.position()
            randNumber = random.randint(2, 4)
            if(randNumber == 1):
                clickRandom(loc[index], max, clickSpeed, 0, 0)
            if(randNumber == 2):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[0], offsetLoc[1])
            elif(randNumber == 3):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[1], offsetLoc[2])
            elif(randNumber == 4):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[0], offsetLoc[2])
            mouseMoveSmooth(
                currentLoc[0],
                (loc[index+1][0]+int(str(time.time())[-1:])) +
                random.randint(-9, 9),
                currentLoc[1],
                (loc[index+1][1]+int(str(time.time())[-1:])) +
                random.randint(-9, 9),
                round(random.uniform(0.1, 0.3), 10)
            )
            sleepRandom(0, 1)
            pyautogui.click(
                duration=round(random.uniform(0.05, 0.075), 10),
                # tween=getTween(),
                _pause=True
            )
            sleepRandom(0, 2)
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
                currentLoc[1]+yIncrement+random.randint(-baseMove, baseMove),
                round(random.uniform(0.05, 0.075), 10)
            )
            currentLoc = pyautogui.position()
            # pyautogui.moveTo(
            #     currentLoc,
            #     duration=round(random.uniform(0.1, 0.3), 10),
            #     tween=pyautogui.easeInQuad,
            #     _pause=False
            # )
            pyautogui.moveTo(
                currentLoc,
                duration=round(random.uniform(0.1, 0.2), 10),
                tween=getTween(),
                _pause=False
            )

        if(random.randint(1, 10) > 8):
            currentLoc = pyautogui.position()
            mouseMoveSmooth(
                currentLoc[0],
                currentLoc[0]+random.randint(-baseMove, baseMove),
                currentLoc[1],
                currentLoc[1]+random.randint(-baseMove, baseMove),
                round(random.uniform(0.05, 0.1), 10)
            )

        randNumber = random.randint(1, 3)
        if(randNumber == 1):
            clickRandom(loc[index+1], max, clickSpeed, -
                        offsetLoc[0], -offsetLoc[1])
        elif(randNumber == 2):
            clickRandom(loc[index+1], max, clickSpeed,
                        offsetLoc[1], offsetLoc[2])
        elif(randNumber == 3):
            clickRandom(loc[index+1], max, clickSpeed,
                        offsetLoc[2], offsetLoc[0])
        currentLoc = pyautogui.position()
        diffX = getDiff(currentLoc[0], loc[index+1][0])
        diffY = getDiff(currentLoc[1], loc[index+1][1])
        if (abs(diffX) < 15 and abs(diffY) < 15):
            currentLoc = pyautogui.position()
            randNumber = random.randint(2, 4)
            if(randNumber == 1):
                clickRandom(loc[index], max, clickSpeed, 0, 0)
            if(randNumber == 2):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[0], offsetLoc[1])
            elif(randNumber == 3):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[1], offsetLoc[2])
            elif(randNumber == 4):
                clickRandom(loc[index], max, clickSpeed,
                            offsetLoc[0], offsetLoc[2])
            mouseMoveSmooth(
                currentLoc[0],
                (loc[index+1][0]+int(str(time.time())[-1:])) +
                random.randint(-9, 9),
                currentLoc[1],
                (loc[index+1][1]+int(str(time.time())[-1:])) +
                random.randint(-9, 9),
                round(random.uniform(0.75, 0.09), 10)
            )
        sleepRandom(0, 1)
        pyautogui.click(
            duration=round(random.uniform(0.05, 0.075), 10),
            # tween=getTween(),
            _pause=True
        )
        sleepRandom(0, 2)
        foo = input("Debug press enter ")
print(" -- Done\n")
currentLoc = pyautogui.position()
pixelColorItem = pyautogui.screenshot(
    imageFilename=".runningTheMouseScript.png",
    region=(currentLoc[0], currentLoc[1], 1, 1)
).getcolors()
