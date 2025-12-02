TEST = True

if TEST:
    inputFile = "input-test.txt"
else:
    inputFile = "input.txt"


def part1():
    ranges = []
    invalids = []
    with open(inputFile) as f:
        lines = [x.strip() for x in f.readlines()]
    for line in lines:
        ranges += line.split(",")

    # Voor elke idrange begin en einde bepalen, en dan alle ID's aflopen.
    for idrange in ranges:
        begin, end = [int(x) for x in idrange.split("-")]
        for i in range(begin, end+1):
            # als de stringversie van de ID een even lengte heeft, en de eerste helft is identiek aan de tweede
            # dan hebben we een ongeldige ID
            stri = str(i)
            if len(stri) % 2 == 0 and stri[:len(stri)//2] == stri[len(stri)//2:]:
                invalids.append(i)

    print("Part 1:", sum(invalids))


def part2():
    ranges = []
    invalids = []
    with open(inputFile) as f:
        lines = [x.strip() for x in f.readlines()]
    for line in lines:
        ranges += line.split(",")

    for idrange in ranges:
        begin, end = [int(x) for x in idrange.split("-")]
        for i in range(begin, end+1):
            stri = str(i)
            # Nu is een ID ongeldig wanneer het volledig uit herhalingen bestaat. Dit zoeken we door de string
            # in steeds kleinere partjes te knippen, en dan kijken of de set van alle partjes uit 1 item bestaat.
            # Is dat het geval, dan is de ID ongeldig.
            # Let op: een ID als 222222 is op meerdere manieren te knippen die ongeldig zijn, maar hij hoeft maar
            # één keer mee te tellen in het eindresultaat, dus break-en we bij gevonden ongeldige id.
            for j in range(1, len(stri)):
                # Knip de string stri in partjes van lengte j
                partjes = [stri[0+i:j+i] for i in range(0, len(stri), j)]
                # En check of alle partjes identiek zijn. Zo ja, registreren en breaken
                if len(set(partjes)) == 1:
                    invalids.append(i)
                    break

    print("Part 2:", sum(invalids))

if __name__ == "__main__":
    part1()
    part2()
