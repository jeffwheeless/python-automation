import pyautogui
import random
import time

totalTime = 0.0
averageTime = 0.0
total = 0
dryRun = True


def performLeftClick(loc1):
    pyautogui.leftClick(
        loc1[0],  # None,
        loc1[1]  # ,  # None,
        # 0,
        #random.uniform(0.3, 0.7)
    )


def performRightClick(loc1):
    pyautogui.rightClick(
        loc1[0],  # None,
        loc1[1]  # ,  # None,
        # 0,
        #random.uniform(0.3, 0.7)
    )


def sleepRandom(smallInt, largeInt):
    # global totalTime
    sleep = random.uniform(smallInt, largeInt)
    # totalTime = totalTime + sleep
    # sleep = 60 + sleep
    time.sleep(sleep)
    # print(sleep)
    # time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))


def runMain(x, loc1, loc2, loc3, prefix, locA, locB):
    # if (int(x) > 0 and int(x) % 4 == 0):
    #     sleepRandom(30, 60)
    # print(x)
    # current = pyautogui.position()
    # if (
    #     (current[0] >= loc1[0]+12 or current[0] <= loc1[0]-12) and
    #     (current[1] >= loc1[1]+12 or current[1] <= loc1[1]-12)
    # ):
    #     foo = input("Mouse over first position ")
    #     loc1 = pyautogui.position()
    # pyautogui.moveTo(
    #     random.randint(loc1[0]-10, loc1[0]+10),
    #     random.randint(loc1[1]-10, loc1[1]+10),
    #     random.uniform(0.3, 0.7)
    # )
    sleepRandom(0.5, 0.9)
    # performRightClick(loc1)
    # sleepRandom(0.03, 0.2)
    # performLeftClick(loc1)
    # sleepRandom(0.05, 0.2)
    # pyautogui.keyDown('ctrl')
    # sleepRandom(0.1, 0.2)
    # pyautogui.press('r')
    # sleepRandom(0.1, 0.2)
    # pyautogui.keyUp('ctrl')
    # sleepRandom(2, 3)
    # performLeftClick(loc2)
    # sleepRandom(0.1, 0.2)

    # performLeftClick(loc2)
    # sleepRandom(0.2, 0.4)
    # pyautogui.press('space')
    # sleepRandom(0.05, 0.07)

    # performRightClick(locA)
    # sleepRandom(0.5, 0.7)
    # performLeftClick(locB)
    # sleepRandom(1, 2)
    # performLeftClick(loc1)
    # sleepRandom(0.05, 0.07)
    # performLeftClick(loc1)
    # sleepRandom(0.05, 0.07)
    # performLeftClick(loc1)
    # sleepRandom(0.5, 0.7)
    # pyautogui.keyDown('ctrl')
    # sleepRandom(0.03, 0.06)
    # pyautogui.press('c')
    # sleepRandom(0.03, 0.06)
    # pyautogui.keyUp('ctrl')
    # sleepRandom(0.03, 0.06)
    pyautogui.moveTo(
        loc2[0],
        loc2[1],
        random.uniform(0.03, 0.06)
    )
    sleepRandom(0.05, 0.1)
    performLeftClick(loc2)
    sleepRandom(0.2, 0.4)
    # pyautogui.press('space')
    # sleepRandom(2, 2.6)
    # sleepRandom(0.2, 0.4)
    # sleepRandom(2, 2.6)
    performRightClick(loc2)
    sleepRandom(0.2, 0.4)
    # pyautogui.moveTo(
    #     loc3[0],
    #     loc3[1],
    #     random.uniform(0.05, 0.2)
    # )
    sleepRandom(0.05, 0.1)
    performLeftClick(loc3)
    sleepRandom(0.4, 0.7)
    pyautogui.press('left')
    pyautogui.keyDown('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.press('v')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.05, 0.1)
    # pyautogui.write(prefix + '__')
    pyautogui.write('__')
    sleepRandom(0.03, 0.06)
    pyautogui.press('enter')
    sleepRandom(0.7, 1)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.05, 0.1)
    pyautogui.press('w')
    sleepRandom(0.05, 0.1)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.1, 0.2)
    pyautogui.press('esc')
    sleepRandom(0.01, 0.05)
    pyautogui.press('esc')
    sleepRandom(0.2, 0.3)


# foo = input("Mouse over header position ")
# locA = pyautogui.position()
foo = input("Mouse over inspect position ")
locB = pyautogui.position()
# foo = input("Mouse over text position ")
# loc1 = pyautogui.position()
# foo = input("Mouse over item position ")
# loc2 = pyautogui.position()
# foo = input("Mouse over save position ")
# loc3 = pyautogui.position()
# foo = input("Mouse over save position ")
# loc3 = pyautogui.position()

locA = [2901, 884]
# locB = [2980, 1235]
loc1 = [4515, 1686]
loc2 = [3044, 1118]
loc3 = [3085, 1342]
print(loc1)
print(loc2)
print(loc3)
print(locA)
print(locB)
averageTime = 6.0664525860234315
# runs = input("how many runs? ")
# prefix = input("prefix words: ")
prefix = "test"
totalTime = 0
totalTimeTotal = 0
longestRun = 0
shortestRun = 100
while (True == True):
    runs = input("\n\nhow many runs? ")
    runs = int(runs)
    oldprefix = prefix
    # prefix = input("prefix words: ")
    # if (prefix == ""):
    #     prefix = oldprefix
    #     print("Applying previously done prefix")
    if (runs == ""):
        runs = 1
    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
    sleepRandom(0.1, 0.2)

    pyautogui.keyDown('ctrl')
    sleepRandom(0.1, 0.2)
    pyautogui.keyDown('shift')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('shift')

    sleepRandom(0.1, 0.2)
    pyautogui.keyDown('home')
    sleepRandom(1, 1.7)
    pyautogui.keyUp('home')
    sleepRandom(0.5, 0.7)
    performRightClick(locA)
    sleepRandom(0.5, 0.7)
    performLeftClick(locB)
    sleepRandom(2, 2.5)
    pyautogui.keyDown('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.press('tab')
    sleepRandom(0.1, 0.2)
    pyautogui.keyUp('alt')
    sleepRandom(0.1, 0.2)
    pyautogui.moveTo(
        loc1[0],
        loc1[1],
        random.uniform(0.05, 0.2)
    )
    foo = input("Mouse over text position ")
    loc1 = pyautogui.position()
    # performLeftClick(loc1)
    # sleepRandom(0.05, 0.07)
    performLeftClick(loc1)
    sleepRandom(0.05, 0.07)
    performLeftClick(loc1)
    sleepRandom(0.5, 0.7)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.03, 0.06)
    pyautogui.press('c')
    sleepRandom(0.03, 0.06)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.5, 0.7)
    performLeftClick(locA)
    sleepRandom(0.5, 0.7)
    pyautogui.keyDown('ctrl')
    sleepRandom(0.05, 0.1)
    pyautogui.press('w')
    sleepRandom(0.05, 0.1)
    pyautogui.keyUp('ctrl')
    sleepRandom(0.5, 0.7)
    # foo = 100/0

    print("Run Time estimated: " + str(averageTime*runs))
    startTimeTotal = time.time()
    for x in range(0, runs):
        startTime = time.time()
        runMain(x, loc1, loc2, loc3, prefix, locA, locB)
        runTime = (time.time()-startTime)
        totalTime = totalTime + runTime
        print("Run #" + str(x+1) + " took " + str(runTime))
        if (runTime > longestRun):
            longestRun = runTime
        if (runTime < shortestRun):
            shortestRun = runTime

    runTimeTotal = (time.time()-startTimeTotal)
    totalTimeTotal = totalTimeTotal + runTimeTotal

    # pyautogui.keyDown('alt')
    # sleepRandom(0.1, 0.2)
    # pyautogui.press('tab')
    # sleepRandom(0.1, 0.2)
    # pyautogui.keyUp('alt')
    total = total + runs
    print("Range: " + str(shortestRun) + " - " + str(longestRun))
    print("total runs: " + str(total))
    print("Time in Runs: " + str(totalTime))
    averageTime = totalTime/total
    print("Average Time in Runs: " + str(averageTime))
    print("Average Time: " + str(totalTimeTotal/total))
    difference = (totalTimeTotal/total) - averageTime
    if (difference < 0.005):
        print("Difference: <0.005")
    else:
        print("Difference: " + str(difference))
