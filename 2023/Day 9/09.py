inputFile = r"input.txt"

def readInput():
    lines = [x.strip() for x in open(inputFile, "r", encoding="utf-8").read().split("\n")]
    return lines

def getDerivative(sequence):
    if len(sequence) < 2:
        return []
    
    return [sequence[x]-sequence[x-1] for x in range(1,len(sequence))]

def part1(lines):
    result = 0
    for index, line in enumerate(lines):
        if line == "":
            continue
        
        # Steeds de afgeleide berekenen totdat de afgeleide helemaal uit 0'en bestaat
        derivative = [int(x) for x in line.split(" ")]
        history = [derivative]
        while len([x for x in derivative if x == 0]) != len(derivative):
            derivative = getDerivative(derivative)
            history.append(derivative)

        # De lijst met allemaal 0'en is niet interessant
        history.pop()
        # Dan de lijst omdraaien zodat we met de laatste afgeleide beginnen en terugwerken
        history.reverse()
        
        # Nu steeds de laatste waarde van een afgeleide-regel optellen bij het tussenresultaat.
        # Het daadwerkelijk toevoegen aan de lijst is niet nodig, maar debugt wel handig.
        addition = 0
        for i in history:
            addition += i[-1]
            i.append(addition)
        
        #print("Tussenresultaat:", history)
        result += history[-1][-1]
        
    print("Part 1:", result)

def part2(lines):
    result = 0

    for index, line in enumerate(lines):
        if line == "":
            continue
        
        # Steeds de afgeleide berekenen totdat de afgeleide helemaal uit 0'en bestaat
        derivative = [int(x) for x in line.split(" ")]
        history = [derivative]
        while len([x for x in derivative if x == 0]) != len(derivative):
            derivative = getDerivative(derivative)
            history.append(derivative)

        # De lijst met allemaal 0'en is niet interessant
        history.pop()
        # Dan de lijst omdraaien zodat we met de laatste afgeleide beginnen en terugwerken
        history.reverse()
        
        # Nu steeds de vorige eerste waarde aftrekken van de huidige eerste waarde, en dat toevoegen als nieuwe eerste waarde
        previous = 0
        for i in history:
            i.insert(0, i[0]-previous)
            previous = i[0]
        
        #print("Tussenresultaat:", history)
            
        # Alle de eerste waarden van de laatste steeds optellen bij het eindresultaat.
        result += history[-1][0]

    
    print("Part 2:", result)
        
    
lines = readInput()
part1(lines)
part2(lines)