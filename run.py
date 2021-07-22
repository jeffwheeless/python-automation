import pyautogui
import random
import numpy as np
import time
from scipy import interpolate
import math

def drawArea(loc):
    max = 10
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
    numMade = random.randint(3, 15)
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
loc = []
loc.append([552, 304])
loc.append([1041, 652])
# foo = input("Mouse over start position ")
# loc.append(pyautogui.position())
# foo = input("Mouse over end position ")
# loc.append(pyautogui.position())
pyautogui.click(loc[0][0], loc[0][1], _pause=False)
pyautogui.press('delete')

print(loc)

for temp in range(0, 20, 5):
    # loc[0][0] = loc[0][0] + (temp * 10)
    loc[0][1] = loc[0][1] + (temp * 10)
    # loc[1][0] = loc[1][0] + (temp * 10)
    loc[1][1] = loc[1][1] + (temp * 10)
    sections = random.randint(4, 6)
    drawArea(loc[0])
    drawArea(loc[1])
    pyautogui.click(loc[0][0], loc[0][1], _pause=False)
    diffX = getDiff(loc[0][0], loc[1][0])
    xIncrement = round(diffX/sections)
    diffY = getDiff(loc[0][1], loc[1][1])
    yIncrement = round(diffY/sections)

    for i in range(0, sections):
        currentLoc = pyautogui.position()
        diffX = getDiff(currentLoc[0], loc[1][0])
        xIncrement = round(diffX/(sections-i))
        diffY = getDiff(currentLoc[1], loc[1][1])
        yIncrement = round(diffY/(sections-i))
        mouseMoveSmooth(
            currentLoc[0],
            currentLoc[0]+xIncrement+random.randint(-10, 10),
            currentLoc[1],
            currentLoc[1]+yIncrement+random.randint(-10, 10)
        )
        pyautogui.press('x')
        
    pyautogui.dragTo(loc[1][0], loc[1][1], _pause=False)
    pyautogui.click(loc[0][0], loc[0][1], _pause=False)
pyautogui.press('[')
pyautogui.dragTo(loc[0][0], loc[0][1], _pause=False)
