from pynput.mouse import Listener
import time

# global totalTime
# global totalClicks
# global previousTime

totalTime = 0
totalClicks = 0
previousTime = 0

print("Press middle button to reset overall average")


def on_move(x, y):
    foo = 1
    # logging.info("Mouse moved to ({0}, {1})".format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        global totalTime
        global totalClicks
        global previousTime

        currentTime = time.time()
        print('\nMouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        timeTaken = currentTime - previousTime
        print("Recent Click took: " + str(timeTaken))
        if(str(button) == "Button.middle"):
            totalTime = 0
            totalClicks = 0
            print("Clearing")

        if (totalClicks <= 1):
            totalTime = 0
        else:
            totalTime = totalTime + timeTaken
            print("Overall Average: " + str(totalTime/totalClicks))
        totalClicks = 1 + totalClicks
        previousTime = currentTime


with Listener(on_move=on_move, on_click=on_click) as listener:

    listener.join()
