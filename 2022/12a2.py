# Het speelveld
grid = []

# Misschien een vies trucje, maar alle coördinaten worden als string opgeslagen
# omdat ze dan als dictionary index bruikbaar zijn.
start = ""
finish = ""

# Het logboek met alle punten waarvan bekend is wat de lengte tot de finish is
ledger = {}
    
# Haal het startpunt en de finish uit het speelveld (als string dus: "y,x")
def findStartAndFinish():
    global grid
    global start
    global finish
    for index, line in enumerate(grid):
        if "S" in line:
            start = str(index)+","+str(line.find("S"))
        if "E" in line:
            finish = str(index)+","+str(line.find("E"))

# Bereken de hoogte voor een y,x-coördinaat.
# Start = 1, Finish = 26, de rest is de positie in het alfabet
def getElevation(y, x):
    global grid
    elevationLetter = grid[y][x]
    if elevationLetter == "S":
        return 1
    elif elevationLetter == "E":
        return 26
    else:
        return ord(elevationLetter)-97

# Een kandidaat-locatie is een valide stap vanaf de huidige locatie wanneer:
# - Hij niet buiten het speelveld ligt
# - De doelhoogte lager (zonder limiet), gelijk of maximaal 1 niveau hoger is dan de starthoogte
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
    

# Een kandidaat-locatie berekenen gegeven de huidige locatie en een richting
# Inclusief string -> (int, int) -> string omzetting
# Niet mooi, maar werkt
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

# Het vinden van de oplossing:
# - Begin bij het einde
# - Kijk welke rondliggende punten valide stappen zijn
# - Voeg deze toe aan het logboek met afstand = huidige afstand + 1
# - Houd bij welke punten net zijn toegevoegd aan het logboek
# - Herhaal voor alle nieuw toegevoegde punten, net zolang tot er geen nieuw
#   toegevoegde punten meer zijn
# - Als het goed is, is dan van alle punten met een pad naar de finish bekend
#   wat de afstand is vanaf dat punt tot de finish
def findSolutions(finish):
    global ledger
    global start
    recentlyAdded = [finish]

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
        
# Lees het invoerbestand                    
with open("12input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

# Lees de start en finish uit
findStartAndFinish()
print("Start:", start, "->", "Finish:", finish)

# Voeg de finish toe met afstand 0, en start het zoeken
ledger[finish]=0
findSolutions(finish)

# Hopelijk is het startpunt gevonden
if start in ledger:
    print("Gevonden:",ledger[start])
    

