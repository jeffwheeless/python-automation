import pyautogui
import random
import time


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
    if (type == 'add'):
        # print("("+str(loc)+"+"+str(time.time())[-1:], end="")
        # print(")+"+str(random.randint(3, max)), end="")
        foo = (loc+int(str(time.time())[-1:]))+(random.randint(3, max)*1)
        # print("=" + str(foo))
    else:
        # print("("+str(loc)+"-"+str(time.time())[-1:], end="")
        # print(")-"+str(random.randint(3, max)), end="")
        foo = (loc-int(str(time.time())[-1:]))-(random.randint(3, max)*1)
        # print("=" + str(foo))

    return foo


def drawArea(loc, max):
    pyautogui.press('x')
    pyautogui.press('[')
    pyautogui.press('[')
    for x in range(0, max, 10):
        pyautogui.click(loc[0]+9+(max*1), loc[1]+9+(max*1), _pause=False)
        pyautogui.dragTo(loc[0]-9-(max*1), loc[1]+9+(max*1), _pause=False)
        pyautogui.dragTo(loc[0]-9-(max*1), loc[1]-9-(max*1), _pause=False)
        pyautogui.dragTo(loc[0]+9+(max*1), loc[1]-9-(max*1), _pause=False)
        pyautogui.dragTo(loc[0]+9+(max*1), loc[1]+9+(max*1), _pause=False)
        # pyautogui.dragTo(loc[randLoc][0]-x, loc[randLoc][1]+x)
        # pyautogui.dragTo(loc[randLoc][0]+x, loc[randLoc][1]+x, button='left')
        # pyautogui.dragTo(loc[randLoc][0]+x, loc[randLoc][1]-x, button='left')
        # pyautogui.dragTo(loc[randLoc][0]-x, loc[randLoc][1]-x, button='left')
    pyautogui.press('x')
    pyautogui.press(']')
    pyautogui.press(']')


max = 5  # input("Max pixels to go out to ")
go = "y"
clickSpeed = 0.125
total = 0
offsetLoc = [3, 5, 2]
loc = []
foo = input("Mouse over first position ")
# loc[0] = pyautogui.position()
# loc.append([3042, 1066])
loc.append(pyautogui.position())
# pyautogui.leftClick(loc[0][0], loc[0][1], _pause=False)
foo = input("Mouse over first position ")
# loc[1] = pyautogui.position()
loc.append(pyautogui.position())
foo = input("Mouse over first position ")
# loc[2] = pyautogui.position()
loc.append(pyautogui.position())
# loc[0] = [3406, 1298]
pyautogui.leftClick(loc[0][0], loc[0][1], _pause=False)
# loc[0] = [3042, 1066]
# print(format_time())
print(loc[0])
# foo = input("Mouse over first position ")

pyautogui.leftClick(loc[0][0], loc[0][1], _pause=False)
pyautogui.press('delete')
pyautogui.press('p')

drawArea(loc[0], max)
drawArea(loc[1], max)
drawArea(loc[2], max)

while(go == "y"):
    for x in range(1, 250):
        # print(x)
        # current = pyautogui.position()
        # if (
        #     (current[0] >= loc[randLoc][0]+12 or current[0] <= loc[randLoc][0]-12) and
        #     (current[1] >= loc[randLoc][1]+12 or current[1] <= loc[randLoc][1]-12)
        # ):
        randLoc = random.randint(0, 2)
        randNumber = random.randint(1, 4)
        if(randNumber == 1):
            pyautogui.click(
                random.randint(
                    shuffleRandomize(loc[randLoc][0], 'sub', max),
                    shuffleRandomize(loc[randLoc][0], 'add', max)
                ),
                random.randint(
                    shuffleRandomize(loc[randLoc][1], 'sub', max),
                    shuffleRandomize(loc[randLoc][1], 'add', max)
                ),
                _pause=False,
                duration=clickSpeed
            )
        elif(randNumber == 2):
            pyautogui.click(
                random.randint(
                    shuffleRandomize(loc[randLoc][0]-offsetLoc[0], 'sub', max),
                    shuffleRandomize(loc[randLoc][0]-offsetLoc[0], 'add', max)
                ),
                random.randint(
                    shuffleRandomize(loc[randLoc][1]-offsetLoc[1], 'sub', max),
                    shuffleRandomize(loc[randLoc][1]-offsetLoc[1], 'add', max)
                ),
                _pause=False,
                duration=clickSpeed
            )
        elif(randNumber == 3):
            pyautogui.click(
                random.randint(
                    shuffleRandomize(loc[randLoc][0]+offsetLoc[1], 'sub', max),
                    shuffleRandomize(loc[randLoc][0]+offsetLoc[1], 'add', max)
                ),
                random.randint(
                    shuffleRandomize(loc[randLoc][1]+offsetLoc[2], 'sub', max),
                    shuffleRandomize(loc[randLoc][1]+offsetLoc[2], 'add', max)
                ),
                _pause=False,
                duration=clickSpeed
            )
        elif(randNumber == 4):
            pyautogui.click(
                random.randint(
                    shuffleRandomize(loc[randLoc][0]+offsetLoc[2], 'sub', max),
                    shuffleRandomize(loc[randLoc][0]+offsetLoc[2], 'add', max)
                ),
                random.randint(
                    shuffleRandomize(loc[randLoc][1]+offsetLoc[0], 'sub', max),
                    shuffleRandomize(loc[randLoc][1]+offsetLoc[0], 'add', max)
                ),
                _pause=False,
                duration=clickSpeed
            )
        print("==== " + str(x) + " =======")
        # sleepRandom(0.9, 1.4)
        # pyautogui.click(duration=clickSpeed, _pause=False)
        # performLeftClick(loc[0])
        # sleepRandom(0.3, 0.7)
        # performLeftClick(loc[0])
        # sleepRandom(30.6, 52.5)
    total = total + 250
    foo = input("clicked: " + str(total) + " another? (y|n) ")
    clickSpeed = clickSpeed - 0.01
