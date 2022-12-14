grid = []

start = "-1,-1"
finish = "-1,-1"

ledger = {}
recentlyAdded = []

def printGrid():
    global grid
    for y in range(len(grid)):
        output = ""
        for x in range(len(grid[0])):
            position = str(y)+","+str(x)
            if position in ledger:
                output += grid[y][x].upper()
            else:
                output += grid[y][x]
        print(output)
            
    
def findStartAndFinish():
    global grid
    global start
    global finish
    for index, line in enumerate(grid):
        if "S" in line:
            start = str(index)+","+str(line.find("S"))
        if "E" in line:
            finish = str(index)+","+str(line.find("E"))

def getElevation(y, x):
    global grid
    elevationLetter = grid[y][x]
    if elevationLetter == "S":
        return 1
    elif elevationLetter == "E":
        return 26
    else:
        return ord(elevationLetter)-97


def isValidCandidate(candidate, location):
    cy, cx = [int(a) for a in candidate.split(",")]
    ly, lx = [int(a) for a in location.split(",")]
    
    if cy < 0 or cy >= len(grid) or cx < 0 or cx >= len(grid[0]):
        return False
    
    celevation = getElevation(cy, cx)
    lelevation = getElevation(ly, lx)
    
    if celevation < lelevation - 1:
        return False
    
    return True
    

def getDirection(currentPosition, direction):
    candidate = "-1,-1"
    cury, curx = [int(a) for a in currentPosition.split(",")]
    if direction == "up":
        candidate = str(cury-1)+","+str(curx)
    elif direction == "right":
        candidate = str(cury)+","+str(curx+1)
    elif direction == "down":
        candidate = str(cury+1)+","+str(curx)
    elif direction == "left":
        candidate = str(cury)+","+str(curx-1)
    
    return candidate    
    
def findSolutions():
    global ledger
    global start
    global num
    global recentlyAdded

    while len(recentlyAdded) > 0:
        addedThisRun = []
        for location in recentlyAdded:
            distance = ledger[location]
            for direction in ["up", "left", "down", "right"]:
                candidate = getDirection(location, direction)
                if candidate not in ledger:
                    if isValidCandidate(candidate, location):
                        addedThisRun.append(candidate)
                        ledger[candidate] = distance + 1

        recentlyAdded = addedThisRun
        
                    
with open("12input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

findStartAndFinish()
print("Start:", start, "->", "Finish:", finish)

ledger[finish]=0
recentlyAdded.append(finish)

findSolutions()

if start in ledger:
    print("Gevonden:",ledger[start])
    

