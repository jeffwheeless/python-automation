
avgTime = 31.215*4
cballPrice = int(input("How much do cannonballs sell for: "))
steelBarPrice = int(input("How much does a steel bar cost: "))
bondPrice = input("Price of a bond: ")
if (bondPrice == ""):
    bondPrice = 6500000
bondPrice = int(bondPrice)

profit = (cballPrice*4)-steelBarPrice
print("Profit per action is: " + str(profit))
profitPerInv = profit*26
actionToBond = bondPrice/profitPerInv
timeToBond = (actionToBond*avgTime)/60
print(timeToBond)
totalTime = ("Total Time: " +
             str(int((timeToBond) // 60)) + ":" +
             ("0" if ((timeToBond) % 60) < 10 else "") +
             str(round((timeToBond) % 60, 5)))
print(totalTime + " hours\n")
