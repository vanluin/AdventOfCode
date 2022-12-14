
rounds = []
inputFile = "d:\\Coding\\AdventOfCode\\2input.txt"

def calculateScore(him, me):
    shapeScore = 0
    roundScore = 0
    
    X = 1
    Y = 2
    Z = 3
    
    if me == 'X':
        roundScore = 0
    elif me == 'Y':
        roundScore = 3
    elif me == 'Z':
        roundScore = 6
        
    # Y wins from A
    # Z loses from A
    # X draws with A
    # Z wins from B
    # X loses from B
    # Y draws with B
    # X wins from C
    # Y loses from C
    # Z draws with C
    if him == 'A':
        if me == 'X':
            shapeScore = Z
        elif me == 'Y':
            shapeScore = X
        elif me == 'Z':
            shapeScore = Y
    elif him == 'B':
        if me == 'X':
            shapeScore = X
        elif me == 'Y':
            shapeScore = Y
        elif me == 'Z':
            shapeScore = Z
    elif him == 'C':
        if me == 'X':
            shapeScore = Y
        elif me == 'Y':
            shapeScore = Z
        elif me == 'Z':
            shapeScore = X
        
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
        


