file = open("input/day2.txt")

goodReportCount = 0

def removeFirstWrong(levels, increasing):
    for i in range(1, len(levels)):
        change = levels[i] - levels[i - 1]

        if(change == 0 or (change > 0 and not increasing) or (change < 0 and increasing) or (change > 3 or change < -3)):
            levels.pop(i - 1)
            return levels

    return True

def areLevelsValid(levels, increasing):
    for i in range(1, len(levels)):
        change = levels[i] - levels[i - 1]

        if(change == 0):
            return False

        if(change > 0 and not increasing):
            return False

        if(change < 0 and increasing):
            return False

        if(change > 3 or change < -3):
            return False

    return True

def isGoodReport(report):
    levelsI = report.split()
    levelsI = [int(string) for string in levelsI]

    increasing = levelsI[0] - levelsI[1] < 0

    if(areLevelsValid(levelsI, increasing)):
       return True
    
    for i in range(0, len(levelsI)):
        levels = levelsI.copy()
        levels.pop(i)
        
        increasing = levels[0] - levels[1] < 0

        if(areLevelsValid(levels, increasing)):
            return True

    return False

for report in file:
    if(isGoodReport(report)):
        goodReportCount += 1
        
print(goodReportCount)

file.close()
