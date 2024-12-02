file = open("input/day1.txt")

left = []
right = []

for line in file:
    pair = line.split()

    left.append(int(pair[0]))
    right.append(int(pair[1]))

total = 0

sortedLeft = sorted(left)
sortedRight = sorted(right)

for i in range(0, len(sortedLeft)):
    total += abs(sortedLeft[i] - sortedRight[i])

print(total)

file.close()
