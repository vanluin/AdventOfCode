rucksacks = []
inputFile = "d:\\Coding\\AdventOfCode\\3input.txt"

def computeScore(item):
    scoreString = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return scoreString.find(item)

with open(inputFile) as f:
    group = []
    for line in f:
        line = line.strip()
        group.append(line)
        if len(group) == 3:
            rucksacks.append(group)
            group = []

totalScore = 0

for group in rucksacks:
    sack1, sack2, sack3 = group
    for item in sack1:
        if item in sack2 and item in sack3:
            totalScore += computeScore(item)
            break
        
print(totalScore)
