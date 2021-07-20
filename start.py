import pyautogui
import random
# frameinfo.filename, frameinfo.lineno
from inspect import currentframe, getframeinfo


def getNumber(a, b, randIntRange):
    return int(
        round(
            ((a-b)/random.randint(randIntRange[0], randIntRange[1])),
            0
        )
    )


def getAltCoord(suggestedCoord, coord):
    if (suggestedCoord > coord + 50):
        suggestedCoord = suggestedCoord - random.randint(25, 50)
    elif (suggestedCoord < coord - 50):
        suggestedCoord = suggestedCoord + random.randint(25, 50)


def getPartialPoint(coord, current, total):
    # get an inbetween point between the current and end location
    randNumber = random.randint(3, 5)
    # frameinfo = getframeinfo(currentframe())
    # print("(" + str(frameinfo.lineno) + ")\t total: " + str(total))
    diff = current - coord
    if (coord > current):
        diff = coord - current

    # randNumber = random.randint(5, 10)
    # if (diff/50 > 2):
    #     # totalDivided = round(total/3, 0)+1
    #     randNumber = random.randint(5, 10)
    if (total > 5):
        totalDivided = round(total/3, 0)+1
        if (totalDivided <= 0):
            totalDivided = 1
        randNumber = random.randint(1, totalDivided)

    # print(randNumber)

    partialEndPoint = coord - ((coord - current)/randNumber)
    if (current > coord):
        partialEndPoint = coord - ((current - coord)/randNumber)

    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) + ")\t Next endpoint: " +
          str(partialEndPoint))

    return round(partialEndPoint)


def drawLine(x, y, linearX, LinearY):
    current = pyautogui.position()
    pyautogui.press('x')
    # pyautogui.moveTo(linearX, LinearY)
    # pyautogui.leftClick(linearX, LinearY, 0, 0.0005)
    # pyautogui.press('x')
    pyautogui.moveTo(current[0], current[1])
    # pyautogui.leftClick(x, y, 0, 0.05)
    pyautogui.dragTo(x, y, button='left')
    # pyautogui.moveTo(x, y)
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) + ")\t current Location: " +
          str(x) + ', ' + str(y))
    pyautogui.leftClick(x, y, 0, 0.0005)


def realignCoordBeforePlot(coord, diffMethod, endpoint, randInts):
    if (randInts[1] < randInts[0]):
        randInt = random.randint(randInts[1], randInts[0])
    else:
        randInt = random.randint(randInts[0], randInts[1])
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) + ")\t randInt: " + str(randInt))
    if (diffMethod == 'add' and coord <= endpoint):
        coord = coord + randInt
    elif (diffMethod == 'add' and coord >= endpoint):
        coord = coord - randInt

    if (diffMethod == 'subtract' and coord >= endpoint):
        coord = coord - randInt
    elif (diffMethod == 'subtract' and coord <= endpoint):
        coord = coord + randInt

    return coord


def getDiffByCoord(coord1, coordLast):
    randIntFromDifference = coordLast - coord1
    # if (coord1 < coordLast):
    #     randIntFromDifference = coordLast - coord1

    # frameinfo = getframeinfo(currentframe())
    # print("(" + str(frameinfo.lineno) + ")\t Difference: " +
    #       str(randIntFromDifference))
    return randIntFromDifference


def randomDistributeNumber(num):
    randomDistributionNumber = random.randint(1, 10)
    if(randomDistributionNumber <= 5):
        return [num * .4, num * .6]
    elif(randomDistributionNumber > 5 and randomDistributionNumber <= 8):
        return [num * .6, num * .8]

    return [num * .8, num]


def mouseMove(loc1, loc2, coordKeyPrime, coordKeySecond, endPoint):
    randIntRange = [5, 10]
    start = pyautogui.position()[coordKeyPrime]
    endPrimeLoc = endPoint[coordKeyPrime] - \
        getNumber(endPoint[coordKeyPrime], start, randIntRange)
    if (loc1[coordKeyPrime] > endPoint[coordKeyPrime]):
        endPrimeLoc = endPoint[coordKeyPrime] - \
            getNumber(start, endPoint[coordKeyPrime], randIntRange)

    if(start > endPrimeLoc):
        tmp = endPrimeLoc
        endPrimeLoc = start
        start = tmp

    # endSecLoc = endPoint[coordKeySecond] - getNumber(endPoint[coordKeySecond], start, randIntRange)
    # if (loc1[coordKeySecond] > endPoint[coordKeySecond]):
    #     endSecLoc = endPoint[coordKeySecond] - getNumber(start, endPoint[coordKeySecond], randIntRange)
    #     # endSecLoc = endPoint[coordKeySecond] - int(round(((start-endPoint[coordKeySecond])/random.randint(randIntRange[0], randIntRange[1])), 0))

    if (loc1[coordKeySecond] == endPoint[coordKeySecond]):
        endPrimeLoc = endPrimeLoc - \
            random.randint(randIntRange[0], randIntRange[1])

    differenceX = getDiffByCoord(
        pyautogui.position()[coordKeyPrime],
        loc2[coordKeyPrime]
    )
    startRandInt = round((differenceX/2)/2)+3
    endRandInt = round(differenceX/2)+3
    if (differenceX <= 0):
        endRandInt = (round((differenceX/2)/2)-3)*-1
        startRandInt = (round(differenceX/2)-4)*-1

    if (startRandInt > endRandInt):
        tmp = endRandInt
        endRandInt = startRandInt
        startRandInt = tmp
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t differenceX: " + str(differenceX))
    xdiff = 'add'
    if (loc1[0] > loc2[0]):
        xdiff = 'subtract'

    ydiff = 'add'
    if (loc1[1] > loc2[1]):
        ydiff = 'subtract'

    endPrimeLoc = int(round(endPrimeLoc, 0))

    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t start: " + str(start))
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t endPrimeLoc: " + str(endPrimeLoc))
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t startRandInt: " + str(startRandInt))
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t endRandInt: " + str(endRandInt))
    randomItem = random.randint(startRandInt, endRandInt)+1
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) +
          ")\t randomItem: " + str(randomItem))
    for x in range(int(start), int(endPrimeLoc), randomItem):
        current = pyautogui.position()
        differenceY = getDiffByCoord(
            current[coordKeySecond], loc2[coordKeySecond])
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) +
              ")\t differenceY: " + str(differenceY))
        randIntBase = differenceY / 2
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) +
              ")\t randIntBase: " + str(randIntBase))
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) +
              ")\t ydiff: " + str(ydiff))

        justFarEnough = 25
        tooHigh = randIntBase >= justFarEnough
        tooLow = randIntBase <= (justFarEnough * -1)
        if (ydiff == 'subtract'):
            tooHigh = randIntBase <= (justFarEnough * -1)
            tooLow = randIntBase >= justFarEnough

        if(tooHigh):
            randInts = randomDistributeNumber(justFarEnough)
        elif(tooLow):
            randInts = randomDistributeNumber(justFarEnough)

        else:  # if (differenceY > 10):
            print("if issue then its in the else")
            if (randIntBase < 0):
                randInts = [
                    round((randIntBase)+2, 0)*-1,
                    round((randIntBase)+2, 0)*-1
                ]
            elif (randIntBase >= 0):
                randInts = [
                    round((randIntBase)+2, 0),
                    round((randIntBase)+2, 0)
                ]

            if(randInts[0] == 0 or randInts[1] == 0):
                randInts[0] = randInts[0] + 1
                randInts[1] = randInts[1] + 2

        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) +
              ")\t Rand Ints: " + str(randInts))
        y = current[coordKeySecond]
        # if (coordKeySecond == 0):
        #     y = realignCoordBeforePlot(current[coordKeySecond], xdiff,
        #                                endPoint[coordKeySecond], randInts)
        # else:
        y = realignCoordBeforePlot(current[coordKeySecond], ydiff,
                                   endPoint[coordKeySecond], randInts)

        if (y == current[0] or y == current[1]):
            y = y + random.randint(randInts[0], randInts[1])
        if (x == current[0] or x == current[1]):
            if (xdiff == "add"):
                x = x + random.randint(1, 15)
            if (xdiff != "add"):
                x = x + random.randint(-15, -1)

        # if (ydiff == 'add' and current[coordKeySecond] < endPoint[coordKeySecond]):
        #     y = y + random.randint(15, 30)

        slope = (loc2[1] - loc1[1]) / (loc2[0] - loc1[0])
        intercept = loc1[1] - (slope * loc1[0])
        if (coordKeyPrime == 0):
            straight = (slope * current[coordKeyPrime]) + intercept
            getAltCoord(y, straight)
            drawLine(x, y, current[coordKeyPrime], straight)
        else:
            if(slope <= 0):
                slope = 1
            straight = (current[coordKeyPrime] - intercept) / slope
            getAltCoord(x, straight)
            drawLine(y, x, straight, current[coordKeyPrime])


def getThere(loc1, loc2, total):
    current = pyautogui.position()
    partialEndPoint = [
        getPartialPoint(loc2[0], current[0], total),
        getPartialPoint(loc2[1], current[1], total)
    ]
    mouseMove(loc1, loc2, 0, 1, partialEndPoint)
    # else:
    # mouseMove(loc1, loc2, 1, 0, partialEndPoint)


def moveThere(loc1, loc2, total):
    current = pyautogui.position()
    if (
        (
            (current[0] <= (loc2[0]+20) and current[0] >= (loc2[0]-20)) and
            (current[1] <= (loc2[1]+20) and current[1] >= (loc2[1]-20))
        ) or total <= 1
    ):
        pyautogui.dragTo(loc2[0], loc2[1],
                         tween=pyautogui.easeInElastic, button='left')
        # pyautogui.moveTo(loc2[0], loc2[1], 0.0005, pyautogui.easeInElastic)
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) + ")\t Current Pos: " +
              str(pyautogui.position()))
        total = 10
    else:
        total = total - 1
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) + ")\t total: " +
              str(total))
        getThere(loc1, loc2, total)
        moveThere(loc1, loc2, total)


locA = [
    [2950, 1251],
    [3146, 1336],
    # [3225, 1146],
    # [3146, 1336],
]

locB = [
    [3146, 1336],
    [3225, 1146],
    # [3146, 1336],
    # [2950, 1251],
]

pyautogui.moveTo(locA[0][0], locA[0][1])
pyautogui.leftClick()
pyautogui.press('delete')
for i in range(0, len(locA)):
    # loc1 = [932, 216] # top right
    loc1 = locA[i]  # left mid
    # foo = input("Mouse over first position ")
    # loc1 = pyautogui.position()
    print(loc1)

    # loc2 = [1616, 909] # bottom right
    loc2 = locB[i]  # right mid
    # foo = input("Mouse over second possition ")
    # loc2 = pyautogui.position()
    print(loc2)

    runs = 1  # input("Runs: ")

    pyautogui.moveTo(loc1[0], loc1[1])
    pyautogui.leftClick(loc1[0], loc1[1])
    # pyautogui.press('x')
    # for x in range(1, 10, 5):
    #     pyautogui.moveTo(loc1[0]-x, loc1[1]-x)
    #     pyautogui.dragTo(loc1[0]-x, loc1[1]+x, button='left')
    #     pyautogui.dragTo(loc1[0]+x, loc1[1]+x, button='left')
    #     pyautogui.dragTo(loc1[0]+x, loc1[1]-x, button='left')
    #     pyautogui.dragTo(loc1[0]-x, loc1[1]-x, button='left')

    #     pyautogui.moveTo(loc2[0]-x, loc2[1]-x)
    #     pyautogui.dragTo(loc2[0]-x, loc2[1]+x, button='left')
    #     pyautogui.dragTo(loc2[0]+x, loc2[1]+x, button='left')
    #     pyautogui.dragTo(loc2[0]+x, loc2[1]-x, button='left')
    #     pyautogui.dragTo(loc2[0]-x, loc2[1]-x, button='left')

    #     pyautogui.moveTo(loc1[0]+(x*10), loc1[1]+(x*10))
    #     pyautogui.dragTo(loc1[0]+(x*10), loc1[1]+(x*10), button='left')
    #     pyautogui.dragTo(loc1[0]+(x*10), loc1[1]-(x*10), button='left')

    #     pyautogui.moveTo(loc2[0]-(x*10), loc2[1]-(x*10))
    #     pyautogui.dragTo(loc2[0]-(x*10), loc2[1]+(x*10), button='left')
    #     pyautogui.dragTo(loc2[0]-(x*10), loc2[1]-(x*10), button='left')
    #     pyautogui.press('x')
    # pyautogui.leftClick(x, y, 0, 0.05)
    # pyautogui.dragTo(x, y, button='left')
    # pyautogui.dragTo(loc2[0], loc2[1], button='left')

    pyautogui.moveTo(loc1[0], loc1[1])
    pyautogui.leftClick(loc1[0], loc1[1])

    loc1 = [
        loc1[0] + random.randint(-5, 5),
        loc1[1] + random.randint(-5, 5)
    ]

    loc2 = [
        loc2[0] + random.randint(-5, 5),
        loc2[1] + random.randint(-5, 5)
    ]

    for one in range(0, int(runs)):
        total = 10
        pyautogui.moveTo(loc1[0], loc1[1])
        currentstart = pyautogui.position()
        moveThere(loc1, loc2, total)

    # for x in range(loc1[0], loc2[0], random.randint(50, 100)):
    #     pyautogui.moveTo(x, loc1[1])

    # pyautogui.moveTo(loc1[0], loc1[1], 4)
