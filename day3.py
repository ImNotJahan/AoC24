file = open("input/day3.txt")

total = 0
executing = True

def readEnabling(instruction):
    if(instruction == "do()"):
        return 1

    if(instruction == "don't()"):
        return -1

    return 0

def readInstruction(instruction):
    if(instruction[:4] != "mul("):
        return 0

    instruction = instruction[4:-1]
    numbers = instruction.split(",")

    if(len(numbers) != 2):
        return 0

    if(not (numbers[0].isdigit() and numbers[1].isdigit())):
       return 0

    return int(numbers[0]) * int(numbers[1])

memory = file.read()

instruction = ""
for i in range(0, len(memory)):
    if(memory[i] == "m" or memory[i] == "d"):
        instruction = ""

    instruction += memory[i]

    if(memory[i] == ")"):
        en = readEnabling(instruction)

        if(en != 0):
            executing = en == 1
        
        if(executing):
            total += readInstruction(instruction)

        instruction = ""

print(total)

file.close()
