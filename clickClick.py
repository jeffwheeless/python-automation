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

y.append([1058, 405, '', 8, 31.5])
x.append([1236, 582, '', 8, 31.5])
y.append([1057, 876, '', 8, 31.5])
x.append([913, 635, '', 8, 31.5])
loc = [1479, 916, '', 5, 30]
lock = False
total = 0
totalTimeStamped = 0


def sleepRandom(smallInt, largeInt):
    sleep = random.uniform(smallInt, largeInt)
    if (sleep > 10):
        print("Long sleep of: " + str(sleep))

    time.sleep(sleep)
    # time.sleep(random.uniform(smallInt, largeInt))

    if (random.randint(1, 1000) > 900):
        sleepRandom(0, 0.5)

    if (sleep > 0.5):
        if (random.randint(1, 1000) > round(925-largeInt)):
            sleepRandom(1, 2)

        if (random.randint(1, 1000) > round(960-largeInt)):
            sleepRandom(1, 3)

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


def on_press(key):
    global loc
    global lock
    global total, totalTimeStamped
    startTime = 0
    if key == keyboard.Key.up:
        current = pyautogui.position()
        loc = [current[0], current[1], loc[2], loc[3]]
        print("Setting New Location")

    if key == keyboard.Key.down:
        startTime = time.time()
        if (lock == False):
            current = pyautogui.position()
            pyautogui.leftClick(current[0], current[1])
            locationDetermine = random.randint(1, 4)
            
            # modloc = [
            #     random.randint(current[0]-y[1][3], current[0]+y[1][3]),
            #     random.randint(y[1][1]-y[1][3], y[1][1]+y[1][3]),
            # ]
            if locationDetermine == 1:
                modloc = [
                    random.randint(x[0][0]-x[0][3], x[0][0]+x[0][3]),
                    random.randint(current[1]-x[0][3], current[1]+x[0][3]),
                ]
            elif locationDetermine == 2:
                modloc = [
                    random.randint(x[1][0]-x[1][3], x[1][0]+x[1][3]),
                    random.randint(current[1]-x[1][3], current[1]+x[1][3]),
                ]
            elif locationDetermine == 3:
                modloc = [
                    random.randint(current[0]-y[0][3], current[0]+y[0][3]),
                    random.randint(y[0][1]-y[0][3], y[0][1]+y[0][3]),
                ]
            elif locationDetermine == 4:
                modloc = [
                    random.randint(current[0]-y[1][3], current[0]+y[1][3]),
                    random.randint(y[1][1]-y[1][3], y[1][1]+y[1][3]),
                ]
            # pyautogui.moveTo()
            # mouseMove(current[0], current[1], modloc[0], m0odloc[1])
            # sleepRandom(0.01, 0.05)
            pyautogui.leftClick(modloc[0], modloc[1])
            # sleepRandom(0.01, 0.05)

            modlocCurrent = [
                random.randint(current[0]-5, current[0]+5),
                random.randint(current[1]-5, current[1]+5),
            ]
            pyautogui.moveTo(modlocCurrent[0], modlocCurrent[1])
            # mouseMove(modloc[0], modloc[1], current[0], current[1])

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
        totalTimeStamped = totalTimeStamped + runTimeStamped
        averageTimeStamped = totalTimeStamped/total
        print("Iteration took: " + str(runTimeStamped) + "s   \t| Average Time Stamped took: " + str(averageTimeStamped) + "s")


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys
# listenerMouse = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
# listenerMouse.start()  # start to listen on a separate thread
# listenerMouse.join()  # remove if main thread is polling self.keys
while True:
    pass
