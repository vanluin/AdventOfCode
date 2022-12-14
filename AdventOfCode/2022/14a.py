grid = []
rockLines = []
start = [0,500]
abyss = False

lowestX = 500
highestX = 500
lowestY = 1
highestY = 1


# Afdrukken van het speelveld
def printGrid():
    global grid
    for y in range(0, len(grid)):
        line = ""
        for x in range(0, len(grid[0])):
            line += grid[y][x]
        print(str(y).zfill(3), line)
    print("")


# Grid opbouwen aan de hand van de ingelezen regels.
# In drie stappen:
# - Eerst de dimensies berekenen
# - Dan het speelveld van de juiste dimensies opbouwen met lucht "."
# - Dan de punten en lijnen ertussen invullen met "#"
def buildGrid():
    global grid
    global rockLines
    global lowestX
    global highestX
    global highestY

    # 't is wat lelijk, 2x door de invoerfile heen, maar ik wil eerst
    # graag weten hoe breed het speelveld moet zijn
    xs = []
    ys = []
    for line in rockLines:
        lineParts = line.split(" -> ")
        for part in lineParts:
            x,y = [int(c) for c in part.split(",")]
            xs.append(x)
            ys.append(y)

    lowestX = min(xs)
    highestX = max(xs)
    highestY = max(ys)
        
    # Dan een leeg speelveld maken van de juiste breedte en hoogte
    for y in range(highestY+1):
        xs = []
        for x in range(lowestX, highestX+1):
            xs.append(".")
        grid.append(xs)

    # Dan de lijnen trekken
    for line in rockLines:
        lineParts = line.split(" -> ")
        prevX = -1
        prevY = -1
        for part in lineParts:
            x,y = [int(c) for c in part.split(",")]
            grid[y][x-lowestX] = "#"
            
            # Na het eerste punt moet er een lijn worden getrokken van het volgende punt
            # naar het vorige punt. Sorteer de twee punten van laag naar hoog, en markeer
            # alle punten op de lijn
            if prevX > -1:
                fromX = min(x, prevX)
                toX = max(x, prevX)
                fromY = min(y, prevY)
                toY = max(y, prevY)
                for i in range(fromY, toY+1):
                    for j in range(fromX, toX+1):
                        grid[i][j-lowestX] = "#"
            prevX = x
            prevY = y

    # Een fictieve bodem toevoegen. Zodra daar een korrel op komt te liggen,
    # doen we alsof hij in de abyss ligt.
    # De bodem bestaat uit een regel lucht, en een regel rots.
    bottom = []
    for x in range(len(grid[0])):
        bottom.append(".")
    grid.append(bottom)
    
    bottom = []
    for x in range(len(grid[0])):
        bottom.append("#")
    grid.append(bottom)
        

# We kunnen recht naar beneden vallen als er op (y+1, x) niets ligt, en dat
# nog binnen het speelveld valt.
def canDropDown(y,x):
    global grid
    return y < len(grid)-1 and grid[y+1][x] == "."


# We kunnen naar links vallen wanneer er op (y+1, x-1) niets ligt, en dat
# nog binnen het speelveld valt.
def canDropLeft(y,x):
    global grid
    return x >= 0 and y+1 < len(grid)-1 and grid[y+1][x-1] == "."


# We kunnen naar rechts vallen wanneer er op (y+1, x+1) niets ligt, en dat
# nog binnen het speelveld valt.
def canDropRight(y,x):
    global grid
    return x+1 < len(grid[0]) and y+1 < len(grid)-1 and grid[y+1][x+1] == "."


# Laat een korrel zand vallen vanaf de startlocatie
def dropSand():
    global grid
    global start
    global lowestX
    global highestX
    global abyss    
    
    # Startlocatie terugrekenen zodat de linkerkolom = 0 ipv ergens in de 400+
    location = [start[0],start[1]-lowestX] 
    y = location[0]
    x = location[1]
    
    # In een oneindige lus eerst proberen naar beneden te vallen, dan naar links
    # en dan naar rechts. Als alle drie niet lukt, dan blijven en stoppen.
    while True:
        if canDropDown(y,x):
            y += 1
        elif canDropLeft(y,x):
            x -= 1
            y += 1
        elif canDropRight(y,x):
            x += 1
            y += 1
        else:
            break
    
    # als we voorbij de oorpronkelijke maximale y zijn, dan liggen we in de abyss.
    if y >= highestY:
        abyss = True
    grid[y][x] = "o"


if __name__ == '__main__':
    # Invoerbestand inlezen
    with open("14input.txt", "r") as f:
        for line in f:
            rockLines.append(line.strip())

    # Grid opbouwen
    buildGrid()
    
    # 1000 zandkorrels is voor het eerste deel genoeg
    for i in range(1000):
        dropSand()
        if abyss:
            break
    
    # Grid afdrukken
    printGrid()

    # We stoppen als de eerste zandkorrel in de abyss ligt, dus we hoeven geen 1 erbij op te tellen
    print("Oplossing deel 1:", i)


