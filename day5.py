file = open("input/day5.txt")
data = file.read().split("\n \n")
rules = data[0].split("\n")
updates = data[1].split("\n")[:-1]

numsAfter = {}

def parseRules(rules, numsAfter):
    for rule in rules:
        ruleParts = rule.split("|")
        k = int(ruleParts[0])
        v = int(ruleParts[1])

        if(k in numsAfter):
            numsAfter[k].append(v)
        else:
            numsAfter[k] = [v]

def verifyPage(pages, numsAfter):
    for i in range(0, len(pages)):
        for k in range(0, i):
            if(pages[i] in numsAfter):
                if(pages[k] in numsAfter[pages[i]]):
                    return False

    return True

def verifyPages(updates, numsAfter):
    total = 0
    
    for update in updates:
        pages = update.split(",")
        pages = [int(page) for page in pages]
        
        if(verifyPage(pages, numsAfter)):
            total += pages[int((len(pages) - 1) / 2)]

    return total

parseRules(rules, numsAfter)
total = verifyPages(updates, numsAfter)

print(total)

file.close()
