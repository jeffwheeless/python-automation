import pyautogui
import random

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
    randNumber = 1
    print(total)
    if (total > 5):
        totalDivided = round(total/3, 0)+1
        if (totalDivided <= 0):
            totalDivided = 1
        randNumber = random.randint(1, totalDivided)

    partialEndPoint = coord - ((coord - current)/randNumber)
    if (current > coord):
        partialEndPoint = coord - ((current - coord)/randNumber)

    return round(partialEndPoint)


def drawLine(x, y, linearX, LinearY):
    current = pyautogui.position()
    pyautogui.press('x')
    pyautogui.moveTo(linearX, LinearY)
    pyautogui.leftClick(linearX, LinearY, 0, 0.05)
    pyautogui.press('x')
    pyautogui.moveTo(current[0], current[1])
    # pyautogui.leftClick(x, y, 0, 0.05)
    pyautogui.dragTo(x, y, button='left')
    pyautogui.moveTo(x, y)
    print(str(x) + ', ' + str(y))
    pyautogui.leftClick(x, y, 0, 0.05)


def realignCoordBeforePlot(coord, diffMethod, endpoint, randInt):
    if (diffMethod == 'add' and coord <= endpoint):
        coord = coord + random.randint(round(randInt/2), randInt)
    elif (diffMethod == 'add' and coord >= endpoint):
        coord = coord - random.randint(round(randInt/2), randInt)

    if (diffMethod == 'subtract' and coord >= endpoint):
        coord = coord - random.randint(round(randInt/2), randInt)
    elif (diffMethod == 'subtract' and coord <= endpoint):
        coord = coord + random.randint(round(randInt/2), randInt)

    return coord


def mouseMove(coordKeyPrime, coordKeySecond, startRandInt, endRandInt, endPoint):
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

    slope = (loc2[1] - loc1[1]) / (loc2[0] - loc1[0])
    intercept = loc1[1] - (slope * loc1[0])
    for x in range(start, endPrimeLoc, random.randint(startRandInt, endRandInt)):
        current = pyautogui.position()
        # left off here, thinking i need to make the next set of randoms have a range of the difference of current and end point divided by a number
        randIntFromDifference = current[coordKeySecond] - loc2[coordKeySecond]
        # realignCoordBeforePlot(coord, diffMethod, endpoint, randInt)
        if (coordKeySecond == 1):
            y = realignCoordBeforePlot(current[coordKeySecond], ydiff,
                                       endPoint[coordKeySecond], randIntFromDifference)
        elif (coordKeySecond == 0):
            x = realignCoordBeforePlot(current[coordKeySecond], xdiff,
                                       endPoint[coordKeySecond], randIntFromDifference)

        if (y == current[0] or y == current[1]):
            y = y + random.randint(-15, 15)
        if (x == current[0] or x == current[1]):
            x = x + random.randint(-15, 15)

        if (coordKeyPrime == 0):
            straight = (slope * current[coordKeyPrime]) + intercept
            getAltCoord(y, straight)
            drawLine(x, y, current[coordKeyPrime], straight)
        else:
            straight = (current[coordKeyPrime] - intercept) / slope
            getAltCoord(x, straight)
            drawLine(y, x, straight, current[coordKeyPrime])


def getThere(total):
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
    if(random.randint(1, 10) >= 3):
        mouseMove(0, 1, randIntRange[0], randIntRange[1], partialEndPoint)
    else:
        mouseMove(1, 0, randIntRange[0], randIntRange[1], partialEndPoint)


def moveThere(total):
    current = pyautogui.position()
    if (
        (
            (current[0] <= (loc2[0]+10) and current[0] >= (loc2[0]-10)) and
            (current[1] <= (loc2[1]+10) and current[1] >= (loc2[1]-10))
        ) or total <= 1
    ):
        pyautogui.dragTo(loc2[0], loc2[1], button='left')
        pyautogui.moveTo(loc2[0], loc2[1], 0.05, pyautogui.easeInElastic)
        print(pyautogui.position())
        total = 10
    else:
        total = total - 1
        getThere(total)
        moveThere(total)


# loc1 = [932, 216] # top right
# loc1 = [862, 581]  # left mid
foo = input("Mouse over first position ")
loc1 = pyautogui.position()
print(loc1)

# loc2 = [1616, 909] # bottom right
# loc2 = [1696, 577]  # right mid
foo = input("Mouse over second position ")
loc2 = pyautogui.position()
print(loc2)

xdiff = 'add'
if (loc1[0] > loc2[0]):
    xdiff = 'subtract'

ydiff = 'add'
if (loc1[1] > loc2[1]):
    ydiff = 'subtract'

runs = input("Runs: ")
pyautogui.moveTo(loc1[0], loc1[1])
pyautogui.leftClick(loc1[0], loc1[1])
# pyautogui.dragTo(loc2[0], loc2[1], button='left')

pyautogui.press('delete')


for one in range(0, int(runs)):
    total = 10
    pyautogui.moveTo(loc1[0], loc1[1])
    currentstart = pyautogui.position()
    moveThere(total)


# for x in range(loc1[0], loc2[0], random.randint(50, 100)):
#     pyautogui.moveTo(x, loc1[1])

# pyautogui.moveTo(loc1[0], loc1[1], 4)
