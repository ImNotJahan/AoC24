file = open("input/day2.txt")

goodReportCount = 0

for report in file:
    levels = report.split()
    levels = [int(string) for string in levels]
    
    increasing = levels[0] - levels[1] < 0
    
    for i in range(1, len(levels)):
        change = levels[i] - levels[i - 1]

        if(change == 0):
            break

        if(change > 0 and not increasing):
            break

        if(change < 0 and increasing):
            break

        if(change > 3 or change < -3):
            break
    else: # this is called if the last loop does not break
        goodReportCount += 1
        
print(goodReportCount)

file.close()
