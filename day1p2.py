file = open("input/day1.txt")

left = []
right = []

for line in file:
    pair = line.split()

    left.append(int(pair[0]))
    right.append(int(pair[1]))

total = 0

for i in range(0, len(left)):
    total += left[i] * right.count(left[i])

print(total)

file.close()
