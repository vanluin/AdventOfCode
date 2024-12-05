inputFile = r"input.txt"

def readInput():
    lines = []
    with open(inputFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                lines.append(line.strip())
    return lines

def part1(lines):
    score = 0
    for line in lines:
        points = 0
        card, numbers = line.split(":")
        card = card.replace("Card ", "")
        
        winningList, ownedList = numbers.split("|")
        winningNumbers = winningList.split(" ")
        ownedNumbers = ownedList.split(" ")

        #Tellen hoeveel winnende nummers de kaart heeft
        #Het eerste winnende nummer levert 1 punt op, de rest verdubbeld het puntenaantal.
        for ownedNumber in ownedNumbers:
            if ownedNumber != '':
                if ownedNumber in winningNumbers:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
                        
        #Totaalscore berekenen
        score += points
    print("Part 1:", score)
        
    
def part2(lines):
    numberOfCards = {}
    # Initieel bestaan alle kaarten 1 keer
    for i in range(1, len(lines)+1):
        numberOfCards[i] = 1
        
    for line in lines:
        card, numbers = line.split(":")
        card = int(card.replace("Card ", ""))
       
        winningList, ownedList = numbers.split("|")
        winningNumbers = winningList.split(" ")
        ownedNumbers = ownedList.split(" ")
        
        #Tellen hoeveel winnende nummers de kaart heeft
        amountWinning = 0
        for ownedNumber in ownedNumbers:
            if ownedNumber != '':
                if ownedNumber in winningNumbers:
                    amountWinning += 1
    
        #Hier weten we hoeveel winnende nummers een ticket bevat.
        #Zoveel winnende nummers als ticket X bevat, zo veel opvolgende kaarten krijgen extra kopieën (tot maximaal de laatste kaart).
        #Het aantal dat elke opvolgende kaart erbij krijg is gelijk aan het aantal keer dat X zelf voorkomt.
        for i in range(card+1, min(card+(amountWinning)+1, len(lines)+1)):
            numberOfCards[i] = numberOfCards[i] + numberOfCards[card]

    #Even alle kaartaantallen optellen
    totalAmount = 0
    for card in numberOfCards:
        totalAmount += numberOfCards[card]
        
    print("Part 2:", totalAmount)
        
    
lines = readInput()
part1(lines)
part2(lines)