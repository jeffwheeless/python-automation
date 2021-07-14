import pyautogui

while 1 == 1:
    foo = input("Mouse over first position ")
    loc1 = pyautogui.position()
    print(loc1)

    foo = input("Mouse over second position ")
    loc2 = pyautogui.position()
    print(loc2)

    print("Distance: " + str(loc1[0]-loc2[0]) +
          ", " + str(loc1[1]-loc2[1]) + "\n")
