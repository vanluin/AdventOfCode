movements = []
with open("d:\\Dropbox\\Python\\AdventOfCode\\9input.txt", "r") as f:
    for line in f:
        movements.append(line.strip())

#initiele posities beginnen in het midden
positionHead = [0,0]
positionTail = [0,0]

#lijst bezochte posities is leeg
positionsVisited = []

def addPosition(y, x):
    global positionsVisited
    positionsVisited.append(str(y)+" "+str(x))
    
def isTouching(head, tail):
    ydist = abs(head[0]-tail[0])
    xdist = abs(head[1]-tail[1])
    return  (ydist <= 1 and xdist <= 1)

def moveHeadOnePosition(head, direction):
    if direction == "R":
        head[1] += 1
    elif direction == "U":
        head[0] -= 1
    elif direction == "L":
        head[1] -= 1
    elif direction == "D":
        head[0] += 1

def moveTailTowardsHead(head, tail):
    # zelfde rij, dus horizontaal bewegen
    if head[0] == tail[0]:
        tail[1] = (head[1] + tail[1])//2
    # zelfde kolom, dus vertikaal bewegen
    elif head[1] == tail[1]:
        tail[0] = (head[0] + tail[0])//2
    # andere rij en andere kolom, nu diagonaal bewegen
    else:
        xdiff = head[1]-tail[1]
        ydiff = head[0]-tail[0]
        
        #horizontaal 1 positie weg, maar vertikaal 2
        # .H.      .H.
        # ...  ->  .T.
        # T..      ...
        if abs(xdiff) == 1:
            tail[0] += ydiff // 2
            tail[1] = head[1]
        #horizontaal 2 posities weg, vertikaal 1
        # ...      ...
        # ..H  ->  .TH
        # T..      ...
        elif abs(ydiff) == 1:
            tail[1] += xdiff // 2
            tail[0] = head[0]
        #zowel horizontaal als vertikaal 2 posities weg
        # ..H      ..H
        # ...  ->  .T.
        # T..      ...
        else:
            tail[0] += ydiff // 2
            tail[1] += xdiff // 2
    
    addPosition(tail[0],tail[1])

# Startpositie opslaan als bezocht
addPosition(positionTail[0],positionTail[1])

for movement in movements:
    direction, distance = movement.split(" ")
    for i in range(int(distance)):
        # Head één stapje bewegen
        moveHeadOnePosition(positionHead, direction)
        # Als de tail niet meer de head aanraakt, dan bewegen
        if not isTouching(positionHead, positionTail):
            moveTailTowardsHead(positionHead, positionTail)

# de lijst bezochte posities uniek maken via een set
positionsVisited = set(positionsVisited)
# en het aantal berekenen
numPositions = len(positionsVisited)
print(numPositions)

