import datetime
import pyautogui

while 1 == 1:
    width, height = pyautogui.size()
    mouseLoc = pyautogui.position()
    dt = datetime.datetime.now()
    dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute)
    # dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    pixelColor = pyautogui.screenshot(
        imageFilename=".screenshot" + str(dt) + ".png",
        region=(
            mouseLoc[0], mouseLoc[1], 1, 1
        )
    ).getcolors()

    print("Screen Size: %dx%d" % (width, height))
    print("Mouse: " + str(mouseLoc))
    print("RGB: %s" % (pixelColor[0][1].__str__()) + '\n')
