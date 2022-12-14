rucksacks = []
inputFile = "d:\\Coding\\AdventOfCode\\3input.txt"

def computeScore(item):
    scoreString = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return scoreString.find(item)

def splitRucksack(rucksack):
    length = len(rucksack)
    left = rucksack[0:length//2]
    right = rucksack[length//2:]

    return left, right

with open(inputFile) as f:
    for line in f:
        line = line.strip()
        rucksacks.append(line)

totalScore = 0

for sack in rucksacks:
    left,right = splitRucksack(sack)
    for item in left:
        if item in right:
            totalScore += computeScore(item)
            break
        
print(totalScore)
