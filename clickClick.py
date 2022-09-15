import pyautogui
import random
import time
from pynput import mouse
from pynput import keyboard

from modules.mouseAutomation import MouseAutomation
from modules.configHelper import ConfigHelper
from modules.inventory import Inventory


x = []
y = []

y.append([3371, 917, '', 10, 5])
x.append([3528, 1094, '', 10, 5])
y.append([3371, 1319, '', 10, 5])
x.append([3220, 1109, '', 10, 5])
loc = [1479, 916, '', 5, 30]
lock = False
total = 0
totalTimeStamped = 0
low = 1000000
high = 0

# def getRandom(smallInt, largeInt):
    

def sleepRandom(smallInt, largeInt):
    # sleep = random.uniform(smallInt, largeInt)
    sleep = random.random()*.1
    demicalPlace = .1
    # sleep = random.random()
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))

    time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))

    if (random.random()*10 > 8):
        sleepRandom(0, 0.5)

    # if (sleep > 0.5):
    #     if (random.randint(1, 1000) > round(925-largeInt)):
    #         sleepRandom(1, 2)

    #     if (random.randint(1, 1000) > round(960-largeInt)):
    #         sleepRandom(1, 3)

        # if (random.randint(1, 1000) > round(990-largeInt)):
        #     sleepRandom(1, 20)


# def on_move(x, y):
#     logging.info("Mouse moved to ({0}, {1})".format(x, y))
#         sleepRandom(0.01, 0.02)


# def on_click(x, y, button, pressed):
#     global loc
#     global lock
#     print("\nx: " + str(x) + " | y: " + str(y))
#     print("locx: " + str(loc[0]) + " | locy: " + str(loc[1]))
#     if (pressed and lock == False):
#         if (
#             (x >= loc[0] or x <= loc[0]+10)
#             and (y >= loc[1]-10 or y <= loc[1]+10)
#         ):
#             modloc = [
#                 random.randint(loc[0]-loc[3],
#                                loc[0]+loc[3]),
#                 random.randint(loc[1]-loc[3],
#                                loc[1]+loc[3]),
#             ]
#             current = pyautogui.position()
#             mouseMove(x, y, modloc[0], modloc[1])
#             # sleepRandom(0.01, 0.05)
#             performLeftClick(pyautogui.position())
#         # sleepRandom(1, 3)
#             # sleepRandom(0.01, 0.05)
#             mouseMove(modloc[0], modloc[1], x, y)


def on_scroll(x, y, dx, dy):
    global loc
    current = pyautogui.position()
    loc = [current[0], current[1], loc[2], loc[3]]
    # sleepRandom(1, 2)
    
def modifyNumber(number, modify):
    modifiedNumber = number-int(random.random()*modify)
    if (random.random() > 0.5):
        modifiedNumber = number+int(random.random()*modify)
        
    return modifiedNumber

def on_press(key):
    global loc
    global lock
    global total, totalTimeStamped
    global low, high
    startTime = 0
    if key == keyboard.Key.caps_lock:
        startTime = time.time()
        if (lock == False):
            current = pyautogui.position()
            pyautogui.leftClick(current[0], current[1], _pause=False)
            closestX = x[0]
            if (abs(current[0]-x[0][0]) > abs(current[0]-x[1][0])):
                closestX = x[1]
                
            closestY = y[0]
            if (abs(current[1]-y[0][1]) > abs(current[1]-y[1][1])):
                closestY = y[1]
                
            closestAxis = 'x'
            if (abs(current[0]-closestX[0]) > abs(current[1]-closestY[1])):
                closestAxis = 'y'
            
            
            if closestAxis == 'y':
                modloc = [
                    modifyNumber(current[0], closestY[3]),
                    modifyNumber(closestY[1], closestY[3]),
                ]
            elif closestAxis == 'x':
                modloc = [
                    modifyNumber(closestX[0], closestX[3]),
                    modifyNumber(current[1], closestX[3]),
                ]
            time.sleep(random.random()*.1)
            pyautogui.leftClick(modloc[0], modloc[1], _pause=False)
            time.sleep(random.random()*.1)
            pyautogui.moveTo(modifyNumber(current[0], 5), modifyNumber(current[1], 5))

    if key == keyboard.Key.down:
        startTime = time.time()
        if (lock == False):
            current = pyautogui.position()
            pyautogui.leftClick(current[0], current[1], _pause=False)
            closestX = x[0]
            if (abs(current[0]-x[0][0]) > abs(current[0]-x[1][0])):
                closestX = x[1]
                
            closestY = y[0]
            if (abs(current[1]-y[0][1]) > abs(current[1]-y[1][1])):
                closestY = y[1]
                
            closestAxis = 'x'
            if (abs(current[0]-closestX[0]) > abs(current[1]-closestY[1])):
                closestAxis = 'y'
            
            
            if closestAxis == 'y':
                modloc = [
                    modifyNumber(current[0], closestY[3]),
                    modifyNumber(closestY[1], closestY[3]),
                ]
            elif closestAxis == 'x':
                modloc = [
                    modifyNumber(closestX[0], closestX[3]),
                    modifyNumber(current[1], closestX[3]),
                ]
            if (random.random() > 0.7):
                time.sleep(random.random()*0.5)
                pyautogui.leftClick(modloc[0], modloc[1], _pause=False)
            time.sleep(random.random()*0.5)
            pyautogui.leftClick(modloc[0], modloc[1], _pause=False)
            time.sleep(random.random()*0.5)
            pyautogui.moveTo(modifyNumber(current[0], 5), modifyNumber(current[1], 5))

    if key == keyboard.Key.right:
        lock = True if lock == False else False
        print("Locking / Unlocking Program")
        # sleepRandom(15, 16)
        # return False  # stop listener

    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    # if k in ['1', '2', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
    # print('Key pressed: ' + k)
    # return False  # stop listener; remove this if wan
    
    if (startTime != 0): 
        total = total + 1
        runTimeStamped = (time.time()-startTime)
        if (runTimeStamped < low):
            low = runTimeStamped
        if (runTimeStamped > high):
            high = runTimeStamped
        totalTimeStamped = totalTimeStamped + runTimeStamped
        averageTimeStamped = totalTimeStamped/total
        print(f"Iteration took: {runTimeStamped}s   \t| Average Time Stamped took: {averageTimeStamped}s")
        print(f"High: {high}s   \t| Low: {low}s")


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys
# listenerMouse = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
# listenerMouse.start()  # start to listen on a separate thread
# listenerMouse.join()  # remove if main thread is polling self.keys
while True:
    pass
