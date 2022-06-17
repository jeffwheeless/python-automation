from tkinter.tix import InputOnly
import pyautogui
import random
import time


def performLeftClickSleep():
    pyautogui.leftClick(None, None, 0, random.uniform(0.065136, 0.43651))
    sleepRandom(0.1, 0.2)


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    print("Sleeping for: " + str(sleep))
    if (sleep > 3):
        time.sleep(sleep-3)
        for i in range(3, 1):
            time.sleep(1)
            print(" " + str(i) + " ", end=""),
    else:
        time.sleep(sleep)


runs = input("How many locations ")

loc = [[pyautogui.position(), 0, 5, 1]]

for x in range(0, int(runs)):
    print("Run number " + str(x))
    isUselessVar = input("Mouse over the position during the following")
    wait = 0  # input("How long to wait to click there: ")
    waitVariation = 0  # input("Variation in time of clicks: ")
    locVariation = 4  # input("Variation in location: ")
    loc.append([pyautogui.position(), int(locVariation),
               int(wait), int(waitVariation)])

# loc.remove([pyautogui.position(), 0, 5, 1])
loc.pop(0)
print(str(loc))
while True == True:
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    for a in range(1, 4):
        print("\n ============ Run: " + str(a) + " ============ ")
        current = pyautogui.position()
        incrementCount = 1
        for x in loc:
            incrementCount = incrementCount + 1
            currentLoc = x
            print(str(x))
            currentLocX = currentLoc[0][0]
            currentLocY = currentLoc[0][1]
            print(incrementCount)
            # if incrementCount == 29 or incrementCount == 1:
            #     pyautogui.keyUp('shift')
            #     sleepRandom(0.2, 0.45)
            #     isUselessVar = input("Go again? ")
            #     sleepRandom(0.2, 0.45)
            # if incrementCount <= 28:
            #     pyautogui.keyDown('shift')
            # if incrementCount > 27:
            sleepRandom(1.2, 2.7)
            pyautogui.moveTo(
                random.randint(
                    round(currentLocX-(currentLoc[1]))-x[1],
                    round(currentLocX+(currentLoc[1]))+x[1],
                ),
                random.randint(
                    round(currentLocY-(currentLoc[1]))-x[1],
                    round(currentLocY+(currentLoc[1]))+x[1],
                ),
                random.uniform(0.165136, 0.43651)
            )
            sleepRandom(
                0.065413, 0.12
                # round(currentLoc[2]-(currentLoc[3]/2)),
                # round(currentLoc[2]+(currentLoc[3]/2))
            )
            current = pyautogui.position()
            if (
                (current[0] >= currentLocX+12 or current[0] <= currentLocX-12) and
                (current[1] >= currentLocY+12 or current[1] <= currentLocY-12)
            ):
                foo = input("Mouse over position ")
            print("Moving")
            performLeftClickSleep()
            print("Clicking")

            if (random.randint(0, 10) > 9):
                pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))
                sleepRandom(0.2654, 0.4351)
            if (random.randint(0, 100) > 95):
                pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))
                sleepRandom(0.2654, 0.4351)
            # if (random.randint(0, 100) > 98):
            #     sleepRandom(1.2654, 3.4351)

        pyautogui.moveTo(current[0], current[1])
    isUselessVar = input("Go again? ")
