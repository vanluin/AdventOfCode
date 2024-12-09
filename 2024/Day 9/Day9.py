
inputFile = "input.txt"
inputTestFile = "input-test.txt"


def part1():
    # Inlezen van de ene regel
    line = open(inputFile).read().strip()
    # We slaan alles op als afwisselende lijst getallen (de fileID) en '.'
    # Elk fileID en . wordt net zo vaak toegevoegd als de waarde van het getal in de input
    parsedLine = []
    fileid = 0
    for i, c in enumerate(line):
        if int(i) & 1:
            # Als de laatste bit van de positie in de input een 1 is, dan is het oneven en stelt het vrije ruimte voor
            # We voegen dan net zoveel "." aan de parsedLine lijst toe als de waarde van het getal in de input op deze plek
            for j in range(int(c)):
                parsedLine.append(".")
        else:
            # Is de laatste bit een 0, dan is het even en voegen we de fileid net zo vaak toe als de waarde van het getal
            # op deze plek. Daarna hogen we de fileid met 1 op zodat de volgende file 1 id hoger krijgt.
            for j in range(int(c)):
                parsedLine.append(fileid)
            fileid += 1

    # Vervolgens zoeken we herhaald naar de plek van de eerstvolgende "." in de lijst. We poppen het laatste
    # element uit de lijst en wanneer dat zelf geen "." is dan zetten we deze op de gevonden plek.
    # Dit doen we net zo lang tot er geen "." meer is.
    while "." in parsedLine:
        i = parsedLine.index(".")
        c = parsedLine.pop()
        if c != ".":
            parsedLine[i] = c

    # Alle "." zijn nu vervangen of weggepopt, dus we kunnen de fileID's met hun positie in de lijst vermenigvuldigen
    # en dat allemaal bij elkaar optellen.
    checksum = sum([c*pos for pos,c in enumerate(parsedLine)])
    print(checksum)

def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()