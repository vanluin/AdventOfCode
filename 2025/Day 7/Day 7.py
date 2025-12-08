from matplotlib import lines

TEST = False

if TEST:
    inputFile = r"input-test.txt"
else:
    inputFile = r"input.txt"


def part1():
    splitters = []
    start = (-1,-1)

    maxRow = 0
    maxCol = 0
    splitters = []
    curTachyon = []
    with open(inputFile) as f:
        lines = [line.strip() for line in f if line.strip()]
        maxRow = len(lines)
        maxCol = len(lines[0])
        splitters = [(y,x) for y in range(maxRow) for x in range(maxCol) if lines[y][x] == "^"]
        curTachyon = [(y,x) for y in range(maxRow) for x in range(maxCol) if lines[y][x] == "S"]

    timesSplit = 0
    for i in range(1, maxRow):
        newTachyon = []
        for j in range(maxCol):
            if (i-1, j) in curTachyon:
                if (i, j) in splitters:
                    newTachyon.append((i, j-1))
                    newTachyon.append((i, j+1))
                    timesSplit += 1
                else:
                    newTachyon.append((i, j))
        curTachyon = newTachyon

    print(timesSplit)

def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
