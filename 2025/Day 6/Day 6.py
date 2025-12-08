import math

TEST = False

if TEST:
    inputFile = r"input-test.txt"
else:
    inputFile = r"input.txt"


def part1():
    with open(inputFile) as f:
        lines = [line.split() for line in f if line.strip()]

    total = 0
    numProblems = len(lines[0])
    for i in range(numProblems):
        problemLine = [lines[x][i] for x in range(len(lines))]
        numbers, operator = problemLine[:-1], problemLine[-1]
        numbers = map(int, numbers)
        if operator == "*":
            total += math.prod(numbers)
        else:
            total += sum(numbers)

    print("Part 1:", total)


# In deel twee zijn de witruimten belangrijk, aangezien we van boven naar beneden lezen en het
# dus uitmaakt in welke kolom een getal staat.
def part2():
    with open(inputFile) as f:
        lines = [line.rstrip() for line in f if line.strip()]

    # Alle regels dezelfde lengte geven door aan te vullen met spaties waar nodig
    maxLength = max([len(x) for x in lines])
    for i, line in enumerate(lines):
        lines[i] += " "*(maxLength-len(line))

    # Achterhalen waar de kolomscheidingen zitten. Deze vind je door te zoeken waar een kolom is
    # die uit alleen maar spaties bestaat.
    indexColumns = [-1]
    for col in range(maxLength):
        colContent = [lines[x][col] for x in range(len(lines))]
        if set(colContent) == {" "}:
            indexColumns.insert(0, col)
    indexColumns.insert(0, maxLength)

    # Nu de groepjes getallen/operator per kolom een lijst van lijsten zetten
    problems = []
    for i in range(len(indexColumns)-1):
        problems.append([])
        for j in range(len(lines)):
            number = lines[j][indexColumns[i+1]+1:indexColumns[i]]
            problems[i].append(number)

    # We hebben hier dus een lijst met lijstjes getallen/operator uit elke kolom
    # Die splitsen we in de getallen en de operator. Daarna draaien we de getallen zodat de kolommen rijen worden
    # en zetten ze om naar int. Daarna de operator erop loslaten en toevoegen aan het totaal
    total =  0
    for problem in problems:
        numbers, operator = problem[:-1], problem[-1]
        numberLength = len(numbers[0])
        pivotedNumbers = [int("".join(col)) for col in zip(*numbers)]
        if operator.strip() == "*":
            total += math.prod(pivotedNumbers)
        else:
            total += sum(pivotedNumbers)

    print("Part 2:", total)

if __name__ == "__main__":
    part1()
    part2()
