movements = []
with open("d:\\Dropbox\\Python\\AdventOfCode\\9input.txt", "r") as f:
    for line in f:
        movements.append(line.strip())
        
length = 2
knots = []
for i in range(length):
    knots.append([0,0])

positionsVisited = []

def visualise():
    global knots
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    
    for knot in knots:
        if knot[0] < miny:
            miny = knot[0]
        if knot[0] > maxy:
            maxy = knot[0]
        if knot[1] < minx:
            minx = knot[1]
        if knot[1] > maxx:
            maxx = knot[1]
    #print(knots)
    print("Visualisation", miny, maxy, minx, maxx)
    
    for line in range(miny, maxy+1):
        lineText = str(line).rjust(3)+" "
        for point in range(minx, maxx+1):
            pos = "."
            for index, knot in enumerate(knots):
                if knot[0] == line and knot[1] == point:
                    pos = str(index)
                    break
            lineText += pos
        print(lineText)

def addPosition(y, x):
    global positionsVisited
    positionsVisited.append(str(y)+" "+str(x))
    #print(positionsVisited)
    
def isTouching(head, tail):
    ydist = abs(head[0]-tail[0])
    xdist = abs(head[1]-tail[1])
    return  (ydist <= 1 and xdist <= 1)

def moveOnePosition(head, direction):
    if direction == "R":
        head[1] += 1
    elif direction == "U":
        head[0] -= 1
    elif direction == "L":
        head[1] -= 1
    elif direction == "D":
        head[0] += 1

def moveTowards(head, tail, isTailKnot):
    # same row, moving sideways
    if head[0] == tail[0]:
        tail[1] = (head[1] + tail[1])//2
    # same column, moving up/down
    elif head[1] == tail[1]:
        tail[0] = (head[0] + tail[0])//2
    # moving diagonally
    else:
        xdiff = head[1]-tail[1]
        ydiff = head[0]-tail[0]
        
        if abs(xdiff) == 1:
            tail[0] += ydiff // 2
            tail[1] = head[1]
        elif abs(ydiff) == 1:
            tail[1] += xdiff // 2
            tail[0] = head[0]
        else:
            # both y and x are 2 positions away
            tail[0] += ydiff // 2
            tail[1] += xdiff // 2
        
    if isTailKnot:
        addPosition(tail[0],tail[1])

# Add starting position
addPosition(0,0)

for movement in movements:
    direction, distance = movement.split(" ")
    for i in range(int(distance)):
        moveOnePosition(knots[0], direction)
        for knot in range(length-1):
            if not isTouching(knots[knot], knots[knot+1]):
                moveTowards(knots[knot], knots[knot+1], (knot+1 == length-1))


#visualise()
positionsVisited = set(positionsVisited)
numPositions = len(positionsVisited)
print(numPositions)

