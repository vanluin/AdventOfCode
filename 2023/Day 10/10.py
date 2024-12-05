inputFile = r"input.txt"

opposites   = { "S":"N", "N":"S", "W":"E", "E":"W" }
directions  = { "S":(1,0), "N":(-1,0), "W":(0,-1), "E":(0,1) }
connections = { "|":"NS", "-":"WE", "L":"NE", "J":"NW", "7":"WS", "F":"ES"}

def readInput():
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n")
    return lines

def findStart(lines):
    points = [(y, line.find("S")) for y, line in enumerate(lines) if line.find("S") > -1]
    return points[0]

def move(point, direction):
    return (point[0] + directions[direction][0], point[1] + directions[direction][1])

def part1(lines):
    startPoint = findStart(lines)
    print(startPoint)
    # We weten de startvorm niet, dus alle 4 directions proberen
    possibleDirections = []
    for direction in "NSEW":
        newPoint = move(startPoint, direction)
        # Als we vanuit hier al buiten het veld komen, overslaan
        if newPoint[0] < 0 or newPoint[0] >= len(lines[0]) or newPoint[1] < 0 or newPoint[1] > len(lines):
            continue
        # Als het nieuwe punt ground is, dan overslaan
        if lines[newPoint[0]][newPoint[1]] == ".":
            continue
        
        possibleDirections.append((newPoint, direction))
    
    history = []
    print("Possible from start:", possibleDirections)
    for point,direction in possibleDirections:
        print("Trying", direction, "reaching", point)
        history = [startPoint]
        while point not in history:
            history.append(point)
            currentSymbol = lines[point[0]][point[1]]
            nextDirection = connections[currentSymbol].replace(opposites[direction],"")
            if len(nextDirection) == 2:
                # Kennelijk testen we een plek die wel een pijp bevat, maar niet een met een aansluiting naar het vorige punt
                break
            
            #print("Point",point,"CurrentSymbol",currentSymbol,"arriving from",opposites[direction],"so moving", nextDirection)
            point = move(point, nextDirection)
            direction = nextDirection
        
        if point == startPoint:
            print("Loop gevonden met lengte",len(history), "dus verste punt", len(history) // 2)
            return history
        
def part2(lines, loop):
    enclosed = 0
    inside = False
    
    lines = [list(line) for line in lines if line.strip() != ""]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            point = (y, x)
            symbol = lines[y][x]
            if point in loop and symbol in "|JL":
                inside = not inside
            elif symbol not in "-7FS":
                if inside:
                    enclosed += 1
                    lines[y][x] = "#"
                    
    #for y in range(len(lines)):
    #    line = ""
    #    for x in range(len(lines[0])):
    #        line += lines[y][x]
    #    print(line)
    
    print("Part 2:", enclosed)
            


lines=readInput()
loop = part1(lines)
part2(lines, loop)
