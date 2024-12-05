inputFile = r"input.txt"

# Lijst van kaarten met run positie in de lijst als waarde. 0, 1 en X worden niet gebruikt maar zijn ervoor om de rest de goede positie te geven.
# Part 1:
possibleCards  = "0123456789TJQKA"
# Part 2:
possibleCards2 = "0J23456789TXQKA"

# Wat constanten voor de leesbaarheid:
FiveOfAKind  = "7"
FourOfAKind  = "6"
FullHouse    = "5"
ThreeOfAKind = "4"
TwoPair      = "3"
OnePair      = "2"
HighCard     = "1"

def readInput():
    lines = open(inputFile, "r", encoding="utf-8").read().split("\n")
    return lines

def getTypeOfHand(hand):
    # Tel het aantal voorkomens van elke kaart in de hand
    cards = [(card, hand.count(card)) for card in possibleCards if hand.count(card) > 0]
    # Sorteer per aantal voorkomens:
    occurences = {}
    for card in cards:
        value, amount = card
        if amount not in occurences:
            occurences[amount] = [value]
        else:
            occurences[amount].append(value)

    # Bepaal nu welk van de 7 typen hand deze hand is
    if 5 in occurences:
        return FiveOfAKind
    elif 4 in occurences:
        return FourOfAKind
    elif 3 in occurences and 2 in occurences:
        return FullHouse
    elif 3 in occurences:
        return ThreeOfAKind
    elif 2 in occurences and len(occurences[2]) == 2:
        return TwoPair
    elif 2 in occurences:
        return OnePair
    else:
        return HighCard

def getLabelsOfHand(hand, cardValues):
    # Zet elke kaart om naar een 2-positie getal (als string) met J = 11, Q = 12, K = 13 en A = 14
    result = "".join([str(cardValues.index(card)).zfill(2) for card in hand])
    return result

def part1(lines):
    setOfHands = {}
    for line in lines:
        if line.strip() == "":
            continue
        
        hand, value = line.strip().split(" ")
        
        # Maak een string "strength" dat bestaat uit het type van de hand met daaraan vastgeplakt de waarde van elke kaart op 2 posities
        # Dus een TwoPair van "J9988" wordt een aaneenschakeling van "3","11","09","09","08","08"
        type = getTypeOfHand(hand)
        labels = getLabelsOfHand(hand, possibleCards)
        strength = type + labels
        setOfHands[int(strength)] = int(value)
    
    # Sorteer de set op basis van de strength, en loop deze lijst af om de winnings te berekenen
    result = 0
    for index,(strength,value) in enumerate(sorted(setOfHands.items())):
        result += (index+1) * value
    
    print("Part 1:", result)

def upgradeHand(currentType):
    # Bereken wat het hoogst mogelijke type zou zijn als je aan de huidige (deel)hand 1 kaart toevoegt
    if currentType == FiveOfAKind:
        return FiveOfAKind  # De hand is al maximaal
    elif currentType == FourOfAKind:
        return FiveOfAKind  # Vier dezelfden kan maximaal vijf dezelfden worden
    elif currentType == FullHouse:
        return FullHouse    # Bij FullHouse zijn alle 5 kaarten al in gebruik en geen joker, dus niets te verbeteren
    elif currentType == ThreeOfAKind:
        return FourOfAKind  # Bij drie dezelfde kaarten is vier dezelfde kaarten de beste keuze
    elif currentType == TwoPair:
        return FullHouse    # De joker inzetten als een van de twee pair-kaarten levert de hoogste keuze op
    elif currentType == OnePair:
        return ThreeOfAKind # Van OnePair zou je TwoPair of ThreeOfAKind kunnen maken. ThreeOfAKind is beter en maakt (als er nog een joker is) FourOfAKind mogelijk
    elif currentType == HighCard:
        return OnePair      # De joker inzetten als een van de bestaande kaarten levert een paar op
    else:
        assert False, "CurrentType = "+currentType+", wat niet hoort te bestaan"


def part2(lines):
    setOfHands = {}
    for line in lines:
        if line.strip() == "":
            continue
        
        hand, value = line.strip().split(" ")
        
        # Alle J's worden nu uit de hand verwijderd. Daarna wordt van de overgebleven hand het type bepaald, en deze wordt
        # net zovaak "geupgraded" als er J's in de oorspronkelijke hand zaten.
        if "J" in hand:
            numJokers = hand.count("J")
            restOfHand = hand.replace("J", "")
            currentType = getTypeOfHand(restOfHand)
            for i in range(numJokers):
                currentType = upgradeHand(currentType)
            type = currentType
        else:
            type = getTypeOfHand(hand)

        # De sorteerlabels gaan nu volgens de nieuwe waardelijst waarbij een J lager is dan een 2
        labels = getLabelsOfHand(hand, possibleCards2)
        strength = type + labels
        setOfHands[int(strength)] = int(value)
        
    # Sorteer de set op basis van de strength, en loop deze lijst af om de winnings te berekenen
    result = 0
    for index,(strength,value) in enumerate(sorted(setOfHands.items())):
        result += (index+1) * value
    
    print("Part 2:", result)
        
    
lines = readInput()
part1(lines)
part2(lines)