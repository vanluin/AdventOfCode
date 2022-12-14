
rounds = []
inputFile = "d:\\Coding\\AdventOfCode\\2input.txt"

def calculateScore(him, me):
    shapeScore = 0
    roundScore = 0
    
    if me == 'X':
        shapeScore = 1
    elif me == 'Y':
        shapeScore = 2
    elif me == 'Z':
        shapeScore = 3
        
    if him == 'A':
        if me == 'X':
            roundScore = 3
        elif me == 'Y':
            roundScore = 6
        elif me == 'Z':
            roundScore = 0
    elif him == 'B':
        if me == 'X':
            roundScore = 0
        elif me == 'Y':
            roundScore = 3
        elif me == 'Z':
            roundScore = 6
    elif him == 'C':
        if me == 'X':
            roundScore = 6
        elif me == 'Y':
            roundScore = 0
        elif me == 'Z':
            roundScore = 3
        
    return shapeScore + roundScore
        
with open(inputFile) as f:
    for line in f:
        line = line.strip()
        him, me = line.split(" ")
        rounds.append({'him':him, 'me':me})

totalScore = 0
for round in rounds:
    totalScore += calculateScore(round['him'], round['me'])
    
print("Total score:",totalScore)
        


