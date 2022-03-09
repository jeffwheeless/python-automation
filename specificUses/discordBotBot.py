
import time
from datetime import datetime
import pyautogui
import random
from inspect import currentframe, getframeinfo

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
                sleepRandom(2, 4)
            if (random.randint(1, 10) > 4):
                writeSleepEnter('+m clue elite')
                sleepRandom(2, 4)
                writeSleepEnter('+m af')
                sleepRandom(2, 4)
            if (random.randint(1, 10) > 4):
                writeSleepEnter('+m clue hard')
                sleepRandom(2, 4)
                writeSleepEnter('+m af')
                sleepRandom(2, 4)
            if (random.randint(1, 10) > 7):
                altCommand(repeatedWord)
                time.sleep(round(random.uniform(5, 10), 10))
            writeSleepEnter(repeatedWord)


def altCommand(currentCommand):
    sleep = round(random.uniform(0, 1), 10)
    fastActions = [
        '+m train magic',
        '+m train ranged',
        '+m train shared',
        '+st vannaka',  # 40 cmb
        '+st konar',  # 75 cmb
    ]

    # slowActions = [
    #     '+as',
    #     '+chop mahogany logs',  # 50 wc
    #     '+fish swordfish',  # 50
    #     '+mine coal',  # 30 mining
    #     '+mine pure essence',  # 30 mining
    # ]
    if (random.randint(1, 100) > 1):
        writeSleepEnter(
            fastActions[random.randint(0, int(len(fastActions)-1))])
        sleepRandom(2, 4)

    # if (random.randint(1, 100) > 1):
    #     writeSleepEnter(
    #         slowActions[random.randint(0, int(len(slowActions)-1))])
    #     sleepRandom(33*60, 37*60)
    # elif (random.randint(1, 100) > 1):
    #     writeSleepEnter(currentCommand)
    #     sleepRandom(33*60, 37*60)
    # sleepRandom(2, 4)


def writeSleepEnter(typedString):
    print("Giving command: " + typedString)
    pyautogui.write(typedString)
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
    smallTime = random.uniform(32*60, 32.5*60)
    largeTime = random.uniform(32.6*60, 35*60)
    # late night
    if (current_time_hour >= earliestDaysHour and current_time_hour < latestDaysHour):
        smallTime = random.uniform(33*60, 60*60)
        largeTime = random.uniform(70*60, 200*60)

    if (current_time_hour < earliestDaysHour or current_time_hour >= latestDaysHour):
        if (random.randint(1, 10) > 9):
            largeTime = random.uniform(34.1*60, 39.9*60)
        elif (random.randint(1, 10) > 9):
            largeTime = random.uniform(36*60, 42*60)

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
        # '+chop mahogany logs',  # 50 wc
        # '+chop maple logs',  # 45 wc
        # '+chop willow logs',  # 30 wc
        # '+fish monkfish',  'cook monkfish',  # 62
        # '+fish raw karambwan', 'cook karambwan',  # 65
        # '+fish raw shark', 'cook shark',  # 65
        # '+fish swordfish', 'cook swordfish',  # 50
        # '/k barrows',
        # '/k chaos druid',
        # '/k dagannoth prime', '/k dagannoth rex', '/k dagannoth supreme',
        # '/k green dragon', '/k blue dragon',
        # '/k lizardman shaman',
        # '/k sarachnis', '/k vorkath', 'zulrah',
        # '+laps canifis rooftop course',  # 40 agility
        # '+laps falador rooftop course',  # 50 agility
        # '+laps seers\' village rooftop course',  # 60 agility
        # '+mine coal', '+mine coal', '+mine coal', '+mine coal',  # 30 mining
        # '+mine gem rock',  # 40 mining
        # '+mine gold', '+mine mithril',
        # '+mine pure essence',  # 30 mining
        # '+offer big bones',
        # '+offer dagannoth bones',
        # '+offer dragon bones',
        # 'pickpicket master farmer',  # 38 thieving
        # '/minion quest',
        # '+sawmill mahogany logs',
        # 'tithefarm',
    ]
    wordCount = len(repeatedWords)
    print(wordCount)
    iterations = int(round(720 / (int(wordCount) * 30), 0))
    print(iterations)
    # quit()
    for foo in range(0, iterations+5000):
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
        # sleepRandom(32*60, 40*60)
        running = run(mainLocation, repeatedWords, iterations, int(wordCount))
        print("\nTotal Time: " + formatHumanTimeString((iterations*averageTime)))
        # quit()
