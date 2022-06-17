
import time
import pyautogui
import random
import os


def writeSleepEnter(typedString):
    pyautogui.write(typedString)
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('enter')


def sleepRandom(smallInt, largeInt):
    sleep = round(random.uniform(smallInt, largeInt), 10)
    print(formatHumanTimeString(sleep))
    time.sleep(sleep)


def formatHumanTimeString(seconds):
    timeLeftMin = round((seconds) // 60)
    timeLeftSec = ("0" if ((seconds) % 60) <
                   10 else "") + str(round(seconds % 60, 5))
    return str(timeLeftMin) + ":" + str(timeLeftSec)


wordCount = input("Hover over text box location ")
mainLocation = pyautogui.position()
wordCount = input("Hover over sell button location ")
sellbutton = pyautogui.position()

itemsToSell = ["10 Adamant 2h sword", "54 Adamant axe", "12 Adamant battleaxe", "2 Adamant chainbody", "2 Adamant dagger", "2 Adamant full helm", "1 Adamant helm (h3)", "240 Adamant javelin", "3 Adamant kiteshield", "2 Adamant longsword", "1 Adamant platebody (h3)", "16 Adamant platebody", "5 Adamant platelegs", "3 Adamant scimitar", "1 Adamant sq shield", "2 Ahrim's robeskirt", "8 Ahrim's robetop", "1 Ahrim's staff", "5 Black 2h sword", "8 Black axe", "3 Black boots", "4 Black knife", "1 Black longsword", "3 Black med helm", "1 Black pickaxe", "1 Black platebody (t)", "1 Black platebody", "24 Black sword", "1 Bronze boots", "7 Bronze longsword", "5 Bronze spear", "1 Dharok's greataxe", "1 Dharok's helm", "1 Dharok's platelegs", "3 Dragon 2h sword", "2 Dragon battleaxe", "2 Dragon dagger(p++)", "12 Dragon dagger", "11 Dragon halberd", "4 Dragon longsword", "7 Dragon mace", "10 Dragon med helm", "2 Dragon necklace", "3 Dragon platelegs", "1 Dragon scimitar", "4 Guthan's helm", "1 Guthan's warspear", "1 Iron boots", "22 Iron javelin", "3008 Iron knife", "8 Iron spear", "14 Iron sword", "1 Karil's crossbow", "5 Karil's leathertop", "1 Mithril 2h sword", "10 Mithril axe", "3 Mithril battleaxe", "12 Mithril boots", "4 Mithril chainbody", "2 Mithril full helm", "3 Mithril javelin", "24 Mithril kiteshield", "1170 Mithril knife", "10 Mithril pickaxe", "2 Mithril platebody", "3 Mithril spear", "2 Mithril sq shield",
               "32 Mithril warhammer", "20 Rune 2h sword", "23 Rune axe", "5 Rune battleaxe", "3 Rune chainbody", "13 Rune dagger", "10 Rune full helm", "1 Rune helm (h5)", "157 Rune javelin", "20 Rune kiteshield", "9 Rune knife", "35 Rune longsword", "3 Rune mace", "6 Rune med helm", "70 Rune pickaxe", "13 Rune platebody", "12 Rune platelegs", "18 Rune plateskirt", "2 Rune scimitar", "3 Rune sq shield", "89 Rune thrownaxe", "41 Steel 2h sword", "32 Steel axe", "58 Steel battleaxe", "2 Steel crossbow", "7 Steel dagger", "7 Steel full helm", "62 Steel kiteshield", "1029 Steel knife", "2 Steel longsword", "4 Steel nails", "15 Steel platebody", "5 Steel platelegs", "1 Steel spear", "1 Bandos d'hide body", "1 Bandos d'hide boots", "1 Bandos platelegs", "1 Saradomin chaps", "1 Saradomin d'hide body", "1 Saradomin kiteshield", "2 Saradomin plateskirt", "5 Saradomin sword", "1 Zamorak bracers", "1 Zamorak full helm", "53 Air battlestaff", "668 Battlestaff", "132 Beer", "1875 Cooked meat", "95 Earth battlestaff", "21 Fremennik blade", "15 Fremennik helm", "20 Fremennik shield", "12 Green d'hide chaps", "44 Green firelighter", "611 Hardleather body", "12 Lava battlestaff", "16 Leather body", "53 Leather gloves", "39 Leather vambraces", "10 Mud battlestaff", "28 Red d'hide vambraces", "11 Red gloves", "100 Right eye patch", "630 Ruby harvest", "12 Staff of water", "210 Studded body", "114 Studded chaps", "38 Water battlestaff", ]
itemsToSellLen = len(itemsToSell)
for i in range(0, itemsToSellLen):
    pyautogui.leftClick(
        mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
    writeSleepEnter("+sell " + itemsToSell[i])
    print("Item " + str(i+1) + " of " +
          str(itemsToSellLen) + ": " + itemsToSell[i])
    pyautogui.moveTo(sellbutton[0], sellbutton[1])
    sleepRandom(4, 7)
    current = pyautogui.position()
    if (current[0] != sellbutton[0] and current[1] != sellbutton[1]):
        pause = input("Pausing ")
    pyautogui.leftClick(sellbutton[0], sellbutton[1],
                        0, random.uniform(0.3, 0.7))
    sleepRandom(2, 4)
print("done")
quit()
