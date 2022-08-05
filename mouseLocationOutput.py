import pyautogui

locationRuns = input("How many run locations: ")
locationRuns = int(locationRuns)
loc = []
print("Apped to postion input to add key")
print("alttab to Alt+Tab otherwise write in key")
with open('mouseLocationOutput.txt', 'w') as f:
    f.write("\n")
for temp in range(0, locationRuns):

    with open('mouseLocationOutput.txt', 'a') as f:
        extraKey = input("Mouse over " + str(temp+1) + " position ")
        current = pyautogui.position()
        distVariation = input("Distance variation between clicks ")
        if (distVariation == ""):
            distVariation = "3"

        timeVariation = input("Time between clicks ")
        if (timeVariation == ""):
            timeVariation = "1"

        loc.append([current[0], current[1], extraKey,
                    int(distVariation), int(timeVariation)])
        # loc1 = pyautogui.position()
        # loc1 = [3323, 1086]
        # loc1 = [2800, 700]
        # loc1 = [500, 0]
        print(loc[temp])
        f.write("loc.append(" + str(loc[temp]) + ")\n")
