file = open("input/day4.txt")
data = file.read().split("\n")[:-1]

occurences = 0
lj = len(data[0])
li = len(data)

for i in range(0, li):
    for j in range(0, lj):
        if(data[i][j] != "X"):
            continue

        if(data[i][j:j+4] == "XMAS"):
            occurences += 1

        if(data[i][j-3:j+1] == "SAMX"):
            occurences += 1

        if(i + 3 < li and data[i + 1][j] + data[i + 2][j] + data[i + 3][j] == "MAS"):
            occurences += 1

        if(i - 3 >= 0 and data[i - 1][j] + data[i - 2][j] + data[i - 3][j] == "MAS"):
            occurences += 1

        if(i + 3 < li and j + 3 < lj and data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3] == "MAS"):
            occurences += 1

        if(i + 3 < li and j - 3 >= 0 and data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3] == "MAS"):
            occurences += 1

        if(i - 3 >= 0 and j + 3 < lj and data[i - 1][j + 1] + data[i - 2][j + 2] + data[i - 3][j + 3] == "MAS"):
            occurences += 1

        if(i - 3 >= 0 and j - 3 >= 0 and data[i - 1][j - 1] + data[i - 2][j - 2] + data[i - 3][j - 3] == "MAS"):
            occurences += 1

print(occurences)

file.close()
