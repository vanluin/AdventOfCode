inputFile = r"17-input-test.txt"

def readInput():
    global lines
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n")
    
lines = None
directions = { "up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1) }
opposites =  { "up":"down", "down":"up", "left":"right", "right":"left" }
cheapest = {}

def getLowest(paths):
    assert len(paths) > 0, "Laagste van lege padlijst"
    lowestIndex = 0
    # Kies als start het eerste pad, daarvan het laatste punt, en daarvan de heatloss
    lowestScore = paths[lowestIndex][-1][3]
    
    for index, path in enumerate(paths):
        if path[-1][3] < lowestScore:
            lowestIndex = index
            lowestScore = path[-1][3]
            
    return lowestIndex

def part1():
    global lines
    # (y, x, direction, heatloss)
    start = (0,0,"down",0)
    dest = (len(lines), len(lines[0]))
    paths = [[start]]
    cheapest[(0,0,"down")]=0
    
    while len(paths) > 0:
        #print("Paths", paths)
        index = getLowest(paths)
        lowestPath = paths.pop(index)
        #print("Positie", index, "is de laagste:", lowestPath)
        # Voor alle richtingen behalve degene waar we vandaan kwamen
        for dir in directions.keys() - { opposites[lowestPath[-1][2]] } :
            #print("Proberen:", dir)
            y, x, prev_dir, heatloss = lowestPath[-1]
            newPoint = (y+directions[dir][0], x+directions[dir][1], opposites[dir])
            
            # Als het nieuwe punt buiten de kaart valt, niet gebruiken
            if newPoint[0] < 0 or newPoint[0] > len(lines)-1 or newPoint[1] < 0 or newPoint[1] > len(lines[0])-1:
                continue
            
            # Als er al een goedkopere manier was om op dit nieuwe punt met deze richting te komen, gebruiken we hem niet
            if newPoint in cheapest:
                continue
            
            # Maximaal 3x dezelfde richting uit
            if len(lowestPath) > 3 and (lowestPath[-1][2] == lowestPath[-2][2] == lowestPath[-3][2] == opposites[dir]):
                continue

            newHeat = heatloss + int(lines[newPoint[0]][newPoint[1]])
            newPath = lowestPath + [(newPoint[0], newPoint[1], newPoint[2], newHeat)]
            cheapest[(newPoint[0], newPoint[1], newPoint[2])] = newHeat
            print("Toegevoegd:", newPoint)
            paths.append(newPath)
            
            if newPoint[0] == dest[0] and newPoint[1] == dest[1]:
                print("Einde bereikt")
                print(newPath)
                paths = []
                break
        #print(10*"-")

 
def part2():
    pass

readInput()
part1()
part2()
