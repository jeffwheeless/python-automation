import pyautogui
import sys
import os

parentDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentDir + '/modules')
import configHelper

config = configHelper.read_config()
locationRuns = input("How many run locations: ")
locationRuns = int(locationRuns)
loc = []
print("Apped to postion input to add key")
print("alttab to Alt+Tab otherwise write in key")
with open('logs/macroLogger.txt', 'w') as f:
    f.write("\n")

for temp in range(0, locationRuns):
    with open('logs/macroLogger.txt', 'a') as f:
        extraKey = input("Mouse over " + str(temp+1) + " position ")
        current = pyautogui.position()
        distVariation = input("Distance variation between clicks ")
        if (distVariation == ""):
            distVariation = config['defaults']['distVariation']

        timeVariation = input("Time between clicks ")
        if (timeVariation == ""):
            timeVariation = config['defaults']['timeVariation']

        loc.append([current[0], current[1], extraKey,
                    int(distVariation), int(timeVariation)])
        print(loc[temp])
        f.write("loc.append(" + str(loc[temp]) + ")\n")
