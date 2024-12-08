
inputFile = "input.txt"
inputTestFile = "input-test3.txt"


def part1():
    antennaHash = {}
    newpointList = []
    # Inlezen van de input. Antennes zijn alles wat geen . of # is.
    field = [x.strip() for x in open(inputFile).read().split()]
    antennas = [(row, col) for row,line in enumerate(field) for col,position in enumerate(field[row]) if field[row][col] not in ['.', '#']]

    # Alle antennes per antennetype in een hash stoppen
    for (row, col) in antennas:
        antennaChar = field[row][col]
        if antennaChar not in antennaHash:
            antennaHash[antennaChar] = []
        antennaHash[antennaChar].append((row,col))

    # We hebben nu een antennaHash met daarin per antennetype de lijst coördinaten van
    # de bijhorende antennes
    # Per antennetype nu de paren maken van alle antennes van dat type
    for antennaType in antennaHash:
        pairs = [(x,y) for i,x in enumerate(antennaHash[antennaType]) for y in antennaHash[antennaType][i+1:]]

        # Per paar in de lijst paren de onderlinge afstand bepalen
        for pair in pairs:
            point1, point2 = pair
            dx, dy = (point2[0]-point1[0], point2[1]-point1[1])

            # De nieuwe punten zijn de huidige punten plus en min de gevonden afstand.
            # Omdat dit ook per punt de andere van de twee oplevert en we de originele
            # punten niet mee willen tellen, worden die er weer afgehaald.
            # Er blijven dan 2 punten over, de gezochte interferentiepunten.
            newpoints = [x for x in
                         [(point1[0]-dx,point1[1]-dy),
                          (point1[0]+dx,point1[1]+dy),
                          (point2[0]-dx,point2[1]-dy),
                          (point2[0]+dx,point2[1]+dy)]
                         if x not in [point1, point2]]
            # De nieuwe punten toevoegen aan de lijst met alle nieuwe punten
            newpointList += newpoints

    # De nieuwepuntenlijst ontdubbelen (set-maken) en filteren op alles wat buiten het veld valt
    newpointList = [x for x in set(newpointList) if 0<=x[0]<len(field) and 0<=x[1]<len(field[0])]
    print("Part 1:", len(newpointList))

def part2():
    antennaHash = {}
    newpointList = []
    # Inlezen van de input. Antennes zijn alles wat geen . of # is.
    field = [x.strip() for x in open(inputFile).read().split()]
    # We zijn alleen geïnteresseerd in de coördinaten van de antennes
    antennas = [(row, col) for row,line in enumerate(field) for col,position in enumerate(field[row]) if field[row][col] not in ['.', '#']]

    # Alle antennes per antennetype in een hash stoppen
    for (row, col) in antennas:
        antennaChar = field[row][col]
        if antennaChar not in antennaHash:
            antennaHash[antennaChar] = []
        antennaHash[antennaChar].append((row,col))

    # We hebben nu een antennaHash met daarin per antennetype de lijst coördinaten van
    # de bijhorende antennes. Per antennetype nu de paren maken van alle antennes van dat type
    for antennaType in antennaHash:
        pairs = [(x,y) for i,x in enumerate(antennaHash[antennaType]) for y in antennaHash[antennaType][i+1:]]

        # Per paar in de lijst paren de onderlinge afstand bepalen
        for pair in pairs:
            point1, point2 = pair
            dx, dy = (point2[0]-point1[0], point2[1]-point1[1])

            # De punten zelf doen deze keer wel mee
            newpointList += [point1, point2]

            # Eerst de lijn negatief doortrekken vanaf punt 1, stoppen wanneer we buiten het veld raken
            pointAdded = True
            newpoint = point1
            while pointAdded:
                newpoint = (newpoint[0]-dx, newpoint[1]-dy)
                if 0<=newpoint[0]<len(field) and 0<=newpoint[1]<len(field[0]):
                    newpointList.append(newpoint)
                else:
                    pointAdded = False
            pointAdded = True

            # Dan positief doortrekken vanaf punt 2en stoppen wanneer we buiten het veld vallen
            pointAdded = True
            newpoint = point2
            while pointAdded:
                newpoint = (newpoint[0]+dx, newpoint[1]+dy)
                if 0<=newpoint[0]<len(field) and 0<=newpoint[1]<len(field[0]):
                    newpointList.append(newpoint)
                else:
                    pointAdded = False
            pointAdded = True

    # De nieuwepuntenlijst ontdubbelen (set-maken). Filteren buiten het veld is al gedaan.
    newpointList = set(newpointList)
    print("Part 2:", len(newpointList))


if __name__ == "__main__":
    part1()
    part2()