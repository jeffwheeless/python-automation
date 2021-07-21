import pyautogui
import random
import numpy as np
import time
from scipy import interpolate
import math


def point_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def drawArea(loc):
    max = 25
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
    numMade = 10  # random.randint(3, 15)
    u = np.linspace(0, 1, num=numMade + int(point_dist(x1, y1, x2, y2)/50.0))
    points = interpolate.splev(u, tck)

    # Move mouse.
    duration = 0.1
    timeout = duration / len(points[0])
    point_list = zip(*(i.astype(int) for i in points))
    for point in point_list:
        pyautogui.dragTo(*point, _pause=False)
        time.sleep(timeout)


cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
foo = input("Mouse over start position ")
x1, y1 = pyautogui.position()  # Starting position
foo = input("Mouse over halfway position ")
x2, y2 = pyautogui.position()  # Starting position
foo = input("Mouse over halfway position 2 ")
x2Alt, y2Alt = pyautogui.position()  # Starting position
foo = input("Mouse over final position ")
x3, y3 = pyautogui.position()  # Starting position
foo = input("Mouse over overshoot position ")
x4, y4 = pyautogui.position()  # Starting position
pyautogui.click(x1, y1)
pyautogui.press('delete')
pyautogui.press('p')
drawArea([x1, y1])
drawArea([x2, y2])
drawArea([x2Alt, y2Alt])
drawArea([x3, y3])
pyautogui.moveTo(x1, y1)

for i in range(1, 25):
    x1New = x1 + random.randint(-5, 5)
    x2New = x2 + random.randint(-5, 5)
    x2AltNew = x2Alt + random.randint(-5, 5)
    x3New = x3 + random.randint(-5, 5)
    y1New = y1 + random.randint(-5, 5)
    y2New = y2 + random.randint(-5, 5)
    y2AltNew = y2Alt + random.randint(-5, 5)
    y3New = y3 + random.randint(-5, 5)
    decider = random.randint(1, 10)
    if (decider <= 3):
        print("holder")
    elif (decider >= 8):
        x2New = x2AltNew
        y2New = y2AltNew
    else:
        xHalf = [x2AltNew, x2New]
        if (xHalf[0] > xHalf[1]):
            xHalf = [x2New, x2AltNew]
        yHalf = [y2AltNew, y2New]
        if (yHalf[0] > yHalf[1]):
            yHalf = [y2New, y2AltNew]
        x2New = random.randint(xHalf[0], xHalf[1])
        y2New = random.randint(yHalf[0], yHalf[1])

    mouseMoveSmooth(x1New, x2New, y1New, y2New)
    if (random.randint(1, 10) >= 8):
        mouseMoveSmooth(x2New, x4, y2New, y4)
        xHalf = [x4, x3New]
        if (xHalf[0] > xHalf[1]):
            xHalf = [x3New, x4]
        yHalf = [y4, y3New]
        if (yHalf[0] > yHalf[1]):
            yHalf = [y3New, y4]
        x2New = random.randint(xHalf[0], xHalf[1])
        y2New = random.randint(yHalf[0], yHalf[1])
        mouseMoveSmooth(x4, x3New, y4, y3New)
    else:
        mouseMoveSmooth(x2New, x3New, y2New, y3New)
    pyautogui.moveTo(x1, y1)
