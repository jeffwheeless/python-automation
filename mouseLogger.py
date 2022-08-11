import pyautogui
import helper

config = helper.read_config()
locationRuns = input("How many run locations: ")
locationRuns = int(locationRuns)
loc = []
print("Apped to postion input to add key")
print("alttab to Alt+Tab otherwise write in key")
with open('mouseLogger.txt', 'w') as f:
    f.write("\n")

for temp in range(0, locationRuns):
    with open('mouseLogger.txt', 'a') as f:
        extraKey = input("Mouse over " + str(temp+1) + " position ")
        current = pyautogui.position()
        loc.append([current[0], current[1]])
        print(loc[temp])
        f.write("loc.append(" + str(loc[temp]) + ")\n")
