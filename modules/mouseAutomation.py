import pyautogui
import random
import time
import numpy as np
import time
from scipy import interpolate
import math

cp = random.randint(3, 5)  # Number of control points. Must be at least 2.

class MouseAutomation:
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
        time.sleep(random.uniform(smallInt, largeInt))
        if (random.randint(1, 1000) > 925):
            MouseAutomation.sleepRandom(0, 1)

        if (random.randint(1, 1000) > 950):
            MouseAutomation.sleepRandom(1, 2)

        if (random.randint(1, 1000) > 975):
            MouseAutomation.sleepRandom(1, 3)


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
        degree = 4
        degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
        # Must be less than number of control points.
        # print("cp: " + str(cp) + " || degree: " + str(degree))
        try:
            tck, u = interpolate.splprep(
                [x, y],
                k=degree
            )
        except ValueError:
            print("Exception made and hopefully caught. Exiting now to bathe in success of the fact it worked")
            return False
            # quit()
        # Move upto a certain number of points
        numMade = 10  # random.randint(3, 15)
        u = np.linspace(0, 1, num=numMade + int(MouseAutomation.point_dist(x1, y1, x2, y2)/50.0))
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
                _pause=False, duration=random.uniform(0.03, 0.09)
            )
            # pyautogui.dragTo(*point, _pause=False)
            duration = random.uniform(0.05, 0.25)
            timeout = duration / len(points[0])
            time.sleep(timeout)


    def mouseMove(x1, y1, x2, y2):
        if (
            x1 <= x2+20 and x1 >= x2-20 and
            y1 <= y2+20 and y1 >= y2-20
        ):
            print("Not moving: [" + str(x1) + ", " + str(y1) + "] to [" + str(x2) + ", " + str(y2) + "]")
        elif (
            x1 <= x2+50 and x1 >= x2-50 and
            y1 <= y2+50 and y1 >= y2-50
        ):
            print("Quickly moving: [" + str(x1) + ", " + str(y1) + "] to [" + str(x2) + ", " + str(y2) + "]")
            pyautogui.moveTo(x2, y2)
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

            x1New = x1 + random.randint(-5, 5)
            xHalfNew = xHalf + random.randint(-5, 5)
            xHalfAltNew = xHalfAlt + random.randint(-5, 5)
            x2New = x2 + random.randint(-5, 5)
            y1New = y1 + random.randint(-5, 5)
            yHalfNew = yHalf + random.randint(-5, 5)
            yHalfAltNew = yHalfAlt + random.randint(-5, 5)
            y2New = y2 + random.randint(-5, 5)

            x1New = x1 + random.randint(-10, 10)
            xHalfNew = xHalf + random.randint(-10, 10)
            xHalfAltNew = xHalfAlt + random.randint(-10, 10)
            x2New = x2 + random.randint(-10, 10)
            y1New = y1 + random.randint(-10, 10)
            yHalfNew = yHalf + random.randint(-10, 10)
            yHalfAltNew = yHalfAlt + random.randint(-10, 10)
            y2New = y2 + random.randint(-10, 10)

            decider = random.randint(0, 1)
            if (decider == 0):
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

            MouseAutomation.mouseMoveSmooth(x1New, xHalfNew, y1New, yHalfNew)
            if (random.randint(1, 10) >= 8):
                # current = pyautogui.position()
                # performLeftClick(current)
                MouseAutomation.mouseMoveSmooth(xHalfNew, x2, yHalfNew, y2)
                xHalf = [x2, x2New]
                if (xHalf[0] > xHalf[1]):
                    xHalf = [x2New, x2]
                yHalf = [y2, y2New]
                if (yHalf[0] > yHalf[1]):
                    yHalf = [y2New, y2]
                xHalfNew = random.randint(xHalf[0], xHalf[1])
                yHalfNew = random.randint(yHalf[0], yHalf[1])
                MouseAutomation.mouseMoveSmooth(x2, x2New, y2, y2New)
            else:
                MouseAutomation.mouseMoveSmooth(xHalfNew, x2New, yHalfNew, y2New)
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
                mainLoc[1] + random.randint(-3, 3), random.uniform(0.3, 0.7)
            )
            MouseAutomation.sleepRandom(
                random.uniform(0.4, 0.6),
                random.uniform(0.6, 0.8)
            )
            current = pyautogui.position()

        return current


    def moveWaitClick(x, y, speed=0.1):
        # mouseOutOfRange([x, y])
        # print("Moving")
        pyautogui.moveTo(x, y, speed)
        MouseAutomation.sleepRandom(0.3, 0.6)
        MouseAutomation.mouseOutOfRange([x, y])
        MouseAutomation.performLeftClick(pyautogui.position())


    def modifyLocationMove(x, y, locationVariance):
        modifiedLocation = [
            random.randint(x-locationVariance, x+locationVariance),
                random.randint(y-locationVariance, y+locationVariance),
        ]
        current = pyautogui.position()
        MouseAutomation.mouseMove(current[0], current[1],
                modifiedLocation[0], modifiedLocation[1])

        return modifiedLocation
    