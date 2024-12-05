inputFile = r"input.txt"

def readInput():
    lines = []
    with open(inputFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                lines.append(line.strip())
    return lines

def findFullNumber(line, index):
    result = 0
    leftIndex = index
    rightIndex = index
    while leftIndex >= 0 and line[leftIndex].isdigit():
        leftIndex -= 1
    while rightIndex < len(line) and line[rightIndex].isdigit():
        rightIndex += 1
    
    result = int(line[leftIndex+1:rightIndex])
    return result

def checkForNumbers(line, leftIndex, rightIndex):
    result = []
    
    for i in range(leftIndex, rightIndex+1):
        if line[i].isdigit():
            result += [findFullNumber(line, i)]
    return list(set(result))

def part1(lines):
    partNumbers = []
    for indexRow, line in enumerate(lines):
        for indexCol, c in enumerate(line):
            if not c.isdigit() and c != '.':
                # c is nu een symbool op positie (indexCol, indexRow)
                # nu de regel voor, op en na (indexCol, indexRow) checken, rekeninghoudend met of we op de eerste of laatste regel zitten
                if indexRow > 0:
                    partNumbers += checkForNumbers(lines[indexRow-1], max(0, indexCol-1), min(len(line), indexCol+1))
                partNumbers += checkForNumbers(line, max(0, indexCol-1), min(len(line), indexCol+1))
                if indexRow < len(lines)-1:
                    partNumbers += checkForNumbers(lines[indexRow+1], max(0, indexCol-1), min(len(line), indexCol+1))
    print("Part 1:", sum(partNumbers))
    
def part2(lines):
    gearRatios = []
    for indexRow, line in enumerate(lines):
        for indexCol, c in enumerate(line):
            if c == '*':
                partNumbers = []
                # c is nu een symbool op positie (indexCol, indexRow)
                # nu de regel voor, op en na (indexCol, indexRow) checken, rekeninghoudend met of we op de eerste of laatste regel zitten
                if indexRow > 0:
                    partNumbers += checkForNumbers(lines[indexRow-1], max(0, indexCol-1), min(len(line), indexCol+1))
                partNumbers += checkForNumbers(line, max(0, indexCol-1), min(len(line), indexCol+1))
                if indexRow < len(lines)-1:
                    partNumbers += checkForNumbers(lines[indexRow+1], max(0, indexCol-1), min(len(line), indexCol+1))
                    
                if len(partNumbers) == 2:
                    gearRatios.append(partNumbers[0]*partNumbers[1])
                    
    print("Part 2:", sum(gearRatios))

lines = readInput()
part1(lines)
part2(lines)