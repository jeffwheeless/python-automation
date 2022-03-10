
import time
from datetime import datetime
import pyautogui
import random
from inspect import currentframe, getframeinfo
import re

# foo = input("Hover over alternative window")
# altWindowXY = pyautogui.position()
totalTime = 0.0
averageTime = 0.0
total = 0
dryRun = True
latestDaysHour = 2
earliestDaysHour = 7


def performLeftClick(mainLocation, repeatedWord=""):
    global dryRun
    mainLocation = mouseOutOfRange(mainLocation)
    if (dryRun == False):
        sleep = round(random.uniform(0, 1), 10)
        time.sleep(sleep)
        print("Clicking")
        pyautogui.leftClick(
            mainLocation[0], mainLocation[1], 0, random.uniform(0.3, 0.7))
        if (repeatedWord != ""):
            if (random.randint(1, 10) > 4):
                writeSleepEnter('+m af')
                # sleepRandom(4/10, 10/10)

            for i in range(0, 10):
                altCommand(repeatedWord)

            writeSleepEnter(repeatedWord)
        quit()


def altCommand(currentCommand):
    # time.sleep(round(random.uniform(5, 10), 10))
    # time.sleep(round(random.uniform(1, 3), 10))
    fastActions = [
        '+m train magic',
        '+m train ranged',
        '+m train shared',
        # '+st vannaka',  # 40 cmb
        '+st konar',  # 75 cmb
    ]

    slowActions = [
        '+m clue medium',
        '+m clue hard',  # 50 wc
        '+m clue elite',  # 50
        '+m af',  # 50
    ]
    if (random.randint(1, 100) > 7):
        writeSleepEnter(
            fastActions[random.randint(0, int(len(fastActions)-1))])
        # sleepRandom(2, 5)

    if (random.randint(1, 100) > 9):
        writeSleepEnter(
            slowActions[random.randint(0, int(len(fastActions)-1))])
        # sleepRandom(4/10, 10/10)


def writeSleepEnter(typedString):
    pattern = re.compile("/[A-z]+")
    results = pattern.search(typedString)
    if (results == None):
        writeSleepEnterSimple(typedString)
    elif (results.group(0) != None):
        typedString = re.split(pattern, typedString)
        writeSleepEnterComplex(results.group(0), typedString[1])


def writeSleepEnterSimple(typedString):
    print("Giving command: " + typedString)
    pyautogui.write(typedString)
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('enter')


def writeSleepEnterComplex(pretext, typedString):
    print("Giving command: " + typedString)
    pyautogui.write(pretext)
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('tab')
    time.sleep(round(random.uniform(3, 7), 10))
    pyautogui.write(typedString)
    time.sleep(round(random.uniform(7, 12), 10))
    pyautogui.press('tab')
    time.sleep(round(random.uniform(0, 1), 10))
    pyautogui.press('enter')


def sleepRandom(smallInt, largeInt):
    global totalTime
    global dryRun
    sleep = round(random.uniform(smallInt, largeInt), 10)
    totalTime = totalTime + sleep
    if (dryRun == False):
        print(formatHumanTimeString(sleep))
        time.sleep(sleep)


def mouseOutOfRange(mainLoc):
    current = pyautogui.position()
    if (current[0] >= mainLoc[0]+7 or current[0] <= mainLoc[0]-7):
        pyautogui.moveTo(mainLoc[0], mainLoc[1], random.uniform(0.3, 0.7))
        sleepRandom(random.uniform(0.4, 0.6), random.uniform(0.6, 0.8))
        current = pyautogui.position()

    return current


def performClick(mainLocation, repeatedWord=""):

    global latestDaysHour
    global earliestDaysHour
    now = datetime.now()
    current_time_hour = int(datetime.now().strftime("%H"))
    smallTime = random.uniform(32/10, 32.5/10)
    largeTime = random.uniform(32.6/10, 35/10)
    # late night
    if (current_time_hour >= earliestDaysHour and current_time_hour < latestDaysHour):
        smallTime = random.uniform(33/10, 60/10)
        largeTime = random.uniform(70/10, 200/10)

    if (current_time_hour < earliestDaysHour or current_time_hour >= latestDaysHour):
        if (random.randint(1, 10) > 9):
            largeTime = random.uniform(34.1/10, 39.9/10)
        elif (random.randint(1, 10) > 9):
            largeTime = random.uniform(36/10, 42/10)

    mainLocation = mouseOutOfRange(mainLocation)
    performLeftClick(mainLocation, repeatedWord)
    sleepRandom(smallTime, largeTime)


def formatHumanTimeString(seconds):
    timeLeftMin = round((seconds) // 60)
    timeLeftSec = ("0" if ((seconds) % 60) <
                   10 else "") + str(round(seconds % 60, 5))
    return str(timeLeftMin) + ":" + str(timeLeftSec)


def clickLocations(mainLocation, repeatedWords, iterations, wordCount):
    global total
    global averageTime
    global dryRun
    for i in range(0, iterations):
        if (dryRun == False):
            print("\n============ Run: " + str(i + 1) +
                  " of " + str(iterations) + " ============")
            timeLeft = formatHumanTimeString(
                averageTime * (iterations - i))
            print("==== Time Left: " + str(timeLeft) + " ====")

        for word in range(0, wordCount):
            if (dryRun == True):
                total = total + 1
                performClick(mainLocation)
            elif (dryRun == False):
                mainLocation = mouseOutOfRange(mainLocation)
                random.shuffle(repeatedWords)
                performClick(mainLocation, repeatedWords[word])
    return True


def run(mainLocation, repeatedWords, iterations, wordCount):
    return clickLocations(mainLocation, repeatedWords, iterations, wordCount)


while True == True:
    repeatedWords = [
        '+as',
        # '+bf mithril bar', '+bf gold bar',
        '+chop mahogany logs',  # 50 wc
        # '+chop maple logs',  # 45 wc
        '+chop teak logs',  # 45 wc
        # '+chop willow logs',  # 30 wc
        '+fish monkfish', '+fish monkfish',  'cook monkfish',  # 62
        # '+fish raw karambwan', 'cook karambwan',  # 65
        # '+fish raw shark', 'cook shark',  # 65
        # '+fish swordfish', 'cook swordfish',  # 50
        # '+hunt red salamander', #67 hunter
        '+hunt swamp lizard',  # 43 hunter
        # '+laps canifis rooftop course',  # 40 agility
        # '+laps falador rooftop course',  # 50 agility
        '+laps pol',  # 60 agility
        # '+laps seers\' village rooftop course',  # 60 agility
        '+mine coal', '+mine coal',  # 30 mining
        '+mine gem rock',  # 40 mining
        '+mine gold', '+mine mithril',
        # '+mine pure essence',  # 30 mining
        # '+offer big bones',
        # '+offer dagannoth bones',
        # '+offer dragon bones',
        '+pickpocket master farmer',  # 38 thieving
        '+sawmill mahogany',
        # '+tithefarm',
        '/k barrows',
        '/k chaos druid',
        # '/k dagannoth prime', '/k dagannoth rex', '/k dagannoth supreme',
        '/k General Graardor', '/k Commander Zilyana',  # '/k Kree\'arra',
        '/k green dragon', '/k blue dragon',
        # '/k lizardman shaman',
        # '/k sarachnis', '/k vorkath', 'zulrah',
        '/minion quest',
    ]
    wordCount = len(repeatedWords)
    print(wordCount)
    iterations = int(round(720 / (int(wordCount) * 30), 0))
    print(iterations)
    # quit()
    # for foo in range(0, iterations+5000):
    for foo in range(0, 10):
        if (type(iterations) == str):
            iterations = int(iterations)
        if (iterations <= 0):
            iterations = 140

        mainLocation = pyautogui.position()
        dryRun = True
        dryRunItemCount = 50
        success = clickLocations(
            mainLocation, repeatedWords[0], dryRunItemCount, 1)
        averageTime = totalTime/total
        averageTimeLeftStr = formatHumanTimeString(totalTime/total)
        print("\n\nAverage Time: " + str(averageTimeLeftStr))
        dryRun = False
        # sleepRandom(32/10, 40/10)
        running = run(mainLocation, repeatedWords, iterations, int(wordCount))
        print("\nTotal Time: " + formatHumanTimeString((iterations*averageTime)))
    quit()
