import pyautogui
import random
import time


def performLeftClickSleep():
    pyautogui.leftClick(None, None, 0, random.uniform(0.3, 0.7))
    sleepRandom(0.5, 0.9)


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    print(sleep)
    if (sleep > 10):
        time.sleep(sleep-3)
        for i in range(0, 3):
            time.sleep(1)
            print(" " + str(i) + " ")


runs = input("How many locations ")

loc = [[pyautogui.position(), 0, 5, 1]]

for x in range(0, int(runs)):
    print("Run number " + str(x))
    print("Mouse over the position during the following")
    wait = input("How long to wait to click there: ")
    waitVariation = input("Variation in time of clicks: ")
    locVariation = input("Variation in location: ")
    loc.append([pyautogui.position(), int(locVariation),
               int(wait), int(waitVariation)])

# loc.remove([pyautogui.position(), 0, 5, 1])
loc.pop(0E)
print(str(loc))
for a in range(1, 1200):
    current = pyautogui.position()
    for x in loc:
        currentLoc = x
        print(str(x))
        currentLocX = currentLoc[0][0]
        currentLocY = currentLoc[0][1]
        print("Sleeping")
        sleepRandom(
            round(currentLoc[2]-(currentLoc[3]/2)),
            round(currentLoc[2]+(currentLoc[3]/2))
        )
        print("Sleeping stopping")
        pyautogui.moveTo(
            random.randint(
                round(currentLocX-(currentLoc[1]/2)),
                round(currentLocX+(currentLoc[1]/2)),
            ),
            random.randint(
                round(currentLocY-(currentLoc[1]/2)),
                round(currentLocY+(currentLoc[1]/2)),
            ),
            random.uniform(0.3, 0.7)
        )
        print("Moving")
        performLeftClickSleep()
        print("Clicking")

    pyautogui.moveTo(current[0], current[1])
