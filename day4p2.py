file = open("input/day4.txt")
data = file.read().split("\n")[:-1]

occurences = 0
lj = len(data[0])
li = len(data)

for i in range(1, li - 1):
    for j in range(1, lj - 1):
        if(data[i][j] != "A"):
            continue

        s1 = data[i - 1][j - 1] + "A" + data[i + 1][j + 1]
        s2 = data[i + 1][j - 1] + "A" + data[i - 1][j + 1]

        if((s1 == "MAS" or s1 == "SAM") and (s2 == "MAS" or s2 == "SAM")):
            occurences += 1

print(occurences)

file.close()
