movements = []
with open("d:\\Dropbox\\Python\\AdventOfCode\\9input.txt", "r") as f:
    for line in f:
        movements.append(line.strip())
        
positionHead = [0,0]
positionTail = [0,0]

positionsVisited = []

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

def moveTowards(head, tail):
    # zelfde rij, dus zijwaards bewegen
    if head[0] == tail[0]:
        tail[1] = (head[1] + tail[1])//2
    # zelfde kolom, dus op/neer bewegen
    elif head[1] == tail[1]:
        tail[0] = (head[0] + tail[0])//2
    # diagonaal bewegen
    else:
        xdiff = head[1]-tail[1]
        ydiff = head[0]-tail[0]
        if xdiff > 1:
            tail[1]+=1
            tail[0]=head[0]
        elif xdiff < -1:
            tail[1]-=1
            tail[0]=head[0]
        elif ydiff > 1:
            tail[0]+=1
            tail[1]=head[1]
        elif ydiff < -1:
            tail[0]-=1
            tail[1]=head[1]
    
    addPosition(tail[0],tail[1])

# Add starting position
addPosition(positionTail[0],positionTail[1])

for movement in movements:
    direction, distance = movement.split(" ")
    for i in range(int(distance)):
        moveOnePosition(positionHead, direction)
        if not isTouching(positionHead, positionTail):
            moveTowards(positionHead, positionTail)

positionsVisited = set(positionsVisited)
numPositions = len(positionsVisited)
print(numPositions)

