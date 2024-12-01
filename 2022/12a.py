grid = []

start = [-1,-1]
finish = [-1,-1]

attemptedSolution = []

def findStartAndFinish():
    global grid
    global start
    global finish
    for index, line in enumerate(grid):
        if "S" in line:
            start = [index,line.find("S")]
        if "E" in line:
            finish = [index,line.find("E")]

def getElevation(point):
    global grid
    pointy, pointx = point
    elevationLetter = grid[pointy][pointx]
    if elevationLetter == "S":
        return 0
    elif elevationLetter == "E":
        return 26
    else:
        return ord(elevationLetter)-97

def isValidCandidate(candidate):
    global grid
    global attemptedSolution
    currentPosition = attemptedSolution[-1]
    
    # outside of grid? not a valid candidate
    if candidate[0] < 0 or candidate[0] > len(grid)-1:
        #print("Candidate", candidate, "outside grid vertically")
        return False
    if candidate[1] < 0 or candidate[1] > len(grid[0])-1:
        #print("Candidate", candidate, "outside grid horizontally")        
        return False
    # elevation difference more than 1? not a valid candidate    
    if abs(getElevation(candidate) - getElevation(currentPosition)) > 1:
        #print("Candidate", candidate, "elevation", getElevation(currentPosition), "differs too much from", getElevation(candidate))        
        return False
    #too far away? not a valid candidate
    if abs(candidate[0]-currentPosition[0]) > 1 or abs(candidate[1]-currentPosition[1]) > 1:
        #print("Candidate", candidate, "not adjacent to currentPosition", currentPosition)
        return False
    # else it's a valid candidate
    #print("Candidate", candidate, "is a valid candidate")
    return True

def checkDirection(direction):
    global solutions
    global finish
    global attemptedSolution
    
    currentPosition = attemptedSolution[-1]
        
    candidate = [-1][-1]
    if direction == "up":
        candidate = [currentPosition[0]-1, currentPosition[1]]
    elif direction == "right":
        candidate = [currentPosition[0], currentPosition[1]+1]
    elif direction == "down":
        candidate = [currentPosition[0]+1, currentPosition[1]]
    elif direction == "left":
        candidate = [currentPosition[0], currentPosition[1]-1]
    
    print("At", currentPosition, "checking", direction, candidate, "after", attemptedSolution)
    if candidate in attemptedSolution:
        #print("Candidate", candidate, "already in current solution")
        pass
    else:
        verdict = isValidCandidate(candidate)
        if verdict:
            attemptedSolution.append(candidate)
            findSolutions()
    
    
def findSolutions():
    global finish
    global attemptedSolution
    
    currentPosition = attemptedSolution[-1]
    
    if currentPosition == finish:
        #currentSolution.append(currentPosition)
        print("Found solution!")
        print(len(attemptedSolution)-1, attemptedSolution)
        return
    else:
        #check up
        checkDirection("up")

        #check right
        checkDirection("right")

        #check down
        checkDirection("down")

        #check left
        checkDirection("left")

with open("12input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

findStartAndFinish()
print("Start:", start, "->", "Finish:", finish)
try:
    attemptedSolution.append(start)
    findSolutions()
except Exception as e:
    print("Fout: ", str(e))
