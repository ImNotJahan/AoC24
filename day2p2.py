file = open("input/day2.txt")

goodReportCount = 0

def areLevelsValid(levels):
    increasing = levels[0] - levels[1] < 0
    
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
    
    if(areLevelsValid(levelsI)):
       return True

    # if is not a good report, check if could be by removing one level (brute forced)
    for i in range(0, len(levelsI)):
        levels = levelsI.copy()
        levels.pop(i)
        
        if(areLevelsValid(levels)):
            return True

    return False

for report in file:
    if(isGoodReport(report)):
        goodReportCount += 1
        
print(goodReportCount)

file.close()
