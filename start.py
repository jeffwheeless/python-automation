import pyautogui
import random
# frameinfo.filename, frameinfo.lineno
from inspect import currentframe, getframeinfo

# pyautogui.moveTo(100,100,duration=0.5)


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
    # print("(" + str(frameinfo.lineno) + ") total: " + str(total))
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
    print("(" + str(frameinfo.lineno) + ") Next endpoint: " +
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
    print("(" + str(frameinfo.lineno) + ") current Location: " +
          str(x) + ', ' + str(y))
    pyautogui.leftClick(x, y, 0, 0.0005)


def realignCoordBeforePlot(coord, diffMethod, endpoint, randInts):
    if (randInts[1] < randInts[0]):
        randInt = random.randint(randInts[1], randInts[0])
    else:
        randInt = random.randint(randInts[0], randInts[1])
    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) + ") randInt: " + str(randInt))
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

    frameinfo = getframeinfo(currentframe())
    print("(" + str(frameinfo.lineno) + ") Difference: " +
          str(randIntFromDifference))
    return randIntFromDifference


def mouseMove(loc1, loc2, coordKeyPrime, coordKeySecond, startRandInt, endRandInt, endPoint):
    randIntRange = [5, 10]
    start = pyautogui.position()[coordKeyPrime]
    endPrimeLoc = endPoint[coordKeyPrime] - \
        getNumber(endPoint[coordKeyPrime], start, randIntRange)
    if (loc1[coordKeyPrime] > endPoint[coordKeyPrime]):
        endPrimeLoc = endPoint[coordKeyPrime] - \
            getNumber(start, endPoint[coordKeyPrime], randIntRange)

    # endSecLoc = endPoint[coordKeySecond] - getNumber(endPoint[coordKeySecond], start, randIntRange)
    # if (loc1[coordKeySecond] > endPoint[coordKeySecond]):
    #     endSecLoc = endPoint[coordKeySecond] - getNumber(start, endPoint[coordKeySecond], randIntRange)
    #     # endSecLoc = endPoint[coordKeySecond] - int(round(((start-endPoint[coordKeySecond])/random.randint(randIntRange[0], randIntRange[1])), 0))

    if (loc1[coordKeySecond] == endPoint[coordKeySecond]):
        endPrimeLoc = endPrimeLoc - \
            random.randint(randIntRange[0], randIntRange[1])

    xdiff = 'add'
    if (loc1[0] > loc2[0]):
        xdiff = 'subtract'

    ydiff = 'add'
    if (loc1[1] > loc2[1]):
        ydiff = 'subtract'

    endPrimeLoc = int(round(endPrimeLoc, 0))

    slope = (loc2[1] - loc1[1]) / (loc2[0] - loc1[0])
    intercept = loc1[1] - (slope * loc1[0])
    for x in range(
        int(start),
        int(endPrimeLoc),
        random.randint(startRandInt, endRandInt)
    ):
        current = pyautogui.position()
        # left off here, thinking i need to make the next set of randoms have a range of the difference of current and end point divided by a number
        # getDiffByCoord(coord1, coordLast)
        differenceY = getDiffByCoord(
            current[coordKeySecond], loc2[coordKeySecond])

        if (differenceY < 0):
            frameinfo = getframeinfo(currentframe())
            print("(" + str(frameinfo.lineno) +
                  ")randIntFromDifference is negative, error")
        randIntBase = differenceY / 2
        if(randIntBase >= 25):
            randomDistributionNumber = random.randint(1, 10)
            if(randomDistributionNumber <= 5):
                randInts = [10, 15]
            elif(randomDistributionNumber > 5 and randomDistributionNumber <= 8):
                randInts = [15, 20]
            else:
                randInts = [20, 25]
        elif(randIntBase <= -25):
            randomDistributionNumber = random.randint(1, 10)
            if(randomDistributionNumber <= 5):
                randInts = [-10, -15]
            elif(randomDistributionNumber > 5 and randomDistributionNumber <= 8):
                randInts = [-15, -20]
            else:
                randInts = [-20, -25]
        # if (differenceY <= 5):
        #     randInts = [-3, 3]
        # elif (differenceY <= 10):
        #     randInts = [-5, 5]
        # elif (differenceY <= 20):
        #     randInts = [-10, 10]
        else:  # if (differenceY > 10):
            if (randIntBase < 0):
                randInts = [round(randIntBase/2, 0), round(randIntBase, 0)]
            elif (randIntBase >= 0):
                randInts = [round(randIntBase/2, 0), round(randIntBase, 0)]
        # realignCoordBeforePlot(coord, diffMethod, endpoint, randInt)

        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) +
              ") Rand Ints: " + str(randInts))
        y = current[coordKeySecond]
        if (coordKeySecond == 0):
            y = realignCoordBeforePlot(current[coordKeySecond], xdiff,
                                       endPoint[coordKeySecond], randInts)
        else:
            y = realignCoordBeforePlot(current[coordKeySecond], ydiff,
                                       endPoint[coordKeySecond], randInts)

        if (y == current[0] or y == current[1]):
            # y = y + random.randint(-15, 15)
            y = y + random.randint(randInts[0], randInts[1])
        if (x == current[0] or x == current[1]):
            if (xdiff == "add"):
                x = x + random.randint(1, 15)
            if (xdiff != "add"):
                x = x + random.randint(-15, -1)
            # x = x + random.randint(randInts[0], randInts[1])

        # if (ydiff == 'add' and current[coordKeySecond] < endPoint[coordKeySecond]):
        #     y = y + random.randint(15, 30)

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
    randIntRange = [25, 50]
    # if (total > 4):
    #     randIntRange = [
    #         round(50/total),
    #         round(75/total)
    #     ]

    current = pyautogui.position()

    partialEndPoint = [
        getPartialPoint(loc2[0], current[0], total),
        getPartialPoint(loc2[1], current[1], total)
    ]
    # if(random.randint(1, 10) >= 3):
    mouseMove(loc1, loc2, 0, 1,
              randIntRange[0], randIntRange[1], partialEndPoint)
    # else:
    # mouseMove(loc1, loc2, 1, 0,
    #           randIntRange[0], randIntRange[1], partialEndPoint)


def moveThere(loc1, loc2, total):
    current = pyautogui.position()
    if (
        (
            (current[0] <= (loc2[0]+20) and current[0] >= (loc2[0]-20)) and
            (current[1] <= (loc2[1]+10) and current[1] >= (loc2[1]-20))
        ) or total <= 1
    ):
        pyautogui.dragTo(loc2[0], loc2[1], button='left')
        pyautogui.moveTo(loc2[0], loc2[1], 0.0005, pyautogui.easeInElastic)
        frameinfo = getframeinfo(currentframe())
        print("(" + str(frameinfo.lineno) + ") Current Pos: " +
              str(pyautogui.position()))
        total = 10
    else:
        total = total - 1
        getThere(loc1, loc2, total)
        moveThere(loc1, loc2, total)


# loc1 = [932, 216] # top right
loc1 = [1027, 797]  # left mid
# foo = input("Mouse over first position ")
# loc1 = pyautogui.position()
print(loc1)

# loc2 = [1616, 909] # bottom right
loc2 = [1570, 892]  # right mid
# foo = input("Mouse over second position ")
# loc2 = pyautogui.position()
print(loc2)

runs = input("Runs: ")

pyautogui.moveTo(loc1[0], loc1[1])
pyautogui.leftClick(loc1[0], loc1[1])
pyautogui.press('delete')
pyautogui.press('x')
for x in range(1, 20, 5):
    pyautogui.moveTo(loc1[0]-x, loc1[1]-x)
    pyautogui.dragTo(loc1[0]-x, loc1[1]+x, button='left')
    pyautogui.dragTo(loc1[0]+x, loc1[1]+x, button='left')
    pyautogui.dragTo(loc1[0]+x, loc1[1]-x, button='left')
    pyautogui.dragTo(loc1[0]-x, loc1[1]-x, button='left')

    pyautogui.moveTo(loc2[0]-x, loc2[1]-x)
    pyautogui.dragTo(loc2[0]-x, loc2[1]+x, button='left')
    pyautogui.dragTo(loc2[0]+x, loc2[1]+x, button='left')
    pyautogui.dragTo(loc2[0]+x, loc2[1]-x, button='left')
    pyautogui.dragTo(loc2[0]-x, loc2[1]-x, button='left')
    
    pyautogui.moveTo(loc1[0]+(x*10), loc1[1]+(x*10))
    pyautogui.dragTo(loc1[0]+(x*10), loc1[1]+(x*10), button='left')
    pyautogui.dragTo(loc1[0]+(x*10), loc1[1]-(x*10), button='left')
    
    pyautogui.moveTo(loc2[0]-(x*10), loc2[1]-(x*10))
    pyautogui.dragTo(loc2[0]-(x*10), loc2[1]+(x*10), button='left')
    pyautogui.dragTo(loc2[0]-(x*10), loc2[1]-(x*10), button='left')
    pyautogui.press('x')
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
