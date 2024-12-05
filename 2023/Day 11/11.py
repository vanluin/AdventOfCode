from itertools import combinations
inputFile = r"input.txt"

universeSizeY = 0
universeSizeX = 0

def readInput():
    global universeSizeY, universeSizeX
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n")
    universeSizeY = len(lines)
    universeSizeX = len(lines[0])
    return lines


def expandGalaxies(galaxies, expandSize = 1):
    global universeSizeY, universeSizeX
    # regels toevoegen van achter naar voren
    for i in reversed(range(universeSizeY)):
        # als het y-coördinaat van de regel niet voorkomt in de lijst met y-coördinaten van galaxies, dan is de regel leeg
        if len([y for (y,x) in galaxies if y == i]) == 0:
            for index, point in enumerate(galaxies):
                # Voor alle galaxies met een y-coördinaat hoger dan de lege regel, tel "expandSize" op bij het y-coördinaat
                if point[0] > i:
                    galaxies[index] = (point[0]+expandSize, point[1])
                    
            # Het universum is in de y-as één groter geworden.
            universeSizeY += 1

    # na een lege kolom extra kolommen toevoegen, van achter naar voren
    for i in reversed(range(universeSizeX)):
        # als het x-coördinaat van de kolom niet voorkomt in de lijst met x-coördinaten van galaxies, dan is de kolom leeg
        if len([x for (y,x) in galaxies if x == i]) == 0:
            for index, point in enumerate(galaxies):
                # Voor alle galaxies met een x-coördinaat hoger dan de lege kolom, tel "expandSize" op bij het x-coördinaat
                if point[1] > i:
                    galaxies[index] = (point[0], point[1]+expandSize)
                    
                    galaxies[index] = (point[0], point[1]+expandSize)
                    
            # Het universum is in de y-as één groter geworden.
            universeSizeX += 1
        
    return galaxies


def getDistance(start, finish):
    # De afstand tussen twee punten is de absolute afstand X plus de absolute afstand Y
    xdist = abs(start[1]-finish[1])
    ydist = abs(start[0]-finish[0])
    return xdist + ydist
   

def part1(lines):
    # Verwerk de galaxies als een lijst coördinaten
    galaxies = [(y, x) for y,line in enumerate(lines) for x,char in enumerate(line) if char == "#"]
    # Voeg de lege regels en kolommen toe door de coördinaten op te hogen
    expandedGalaxies = expandGalaxies(galaxies)
    # Verzamel alle paren van punten
    pairs = list(combinations(expandedGalaxies, 2))
    # Tel de som van alle afstanden tussen alle paren op
    print("Part 1:", sum([getDistance(a,b) for (a,b) in pairs]))


def part2(lines):
    # Verwerk de galaxies als een lijst coördinaten
    galaxies = [(y, x) for y,line in enumerate(lines) for x,char in enumerate(line) if char == "#"]
    # Voeg de lege regels en kolommen toe door de coördinaten op te hogen met 999999 (de 1e bestaat al)
    expandedGalaxies = expandGalaxies(galaxies, 999999)
    # Verzamel alle paren van punten
    pairs = list(combinations(expandedGalaxies, 2))
    # Tel de som van alle afstanden tussen alle paren op
    print("Part 2:", sum([getDistance(a,b) for (a,b) in pairs]))


lines=readInput()
part1(lines)
part2(lines)